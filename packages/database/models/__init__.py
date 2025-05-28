from uuid import uuid4
from sqlalchemy import ARRAY, BIGINT, BOOLEAN, DATE, INTEGER, VARCHAR, TEXT, Column, Enum, ForeignKey

from packages.database.enums.offer_tag_groups import OfferTagGroupEnum
from packages.database.enums.offer_tag_names import OfferTagNamesEnum
from .base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


############################################
#                   Users                  #
############################################

class Roles(Base):
    __tablename__ = "roles"
    
    RoleId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    RoleName = Column(VARCHAR(50), nullable=False)
    RoleLevel = Column(INTEGER, nullable=False)
    
    _users = relationship("Users", back_populates="_roles")

class Users(Base):
    __tablename__ = "users"
    
    UserId = Column(UUID(as_uuid=True),primary_key=True, default=uuid4())
    PhoneNumber = Column(VARCHAR(11), nullable=True)
    TelegramId = Column(BIGINT, nullable=False, unique=True)
    IsVip = Column(BOOLEAN, nullable=False)
    RoleId = Column(UUID(as_uuid=True), ForeignKey("roles.RoleId"), nullable=False)
    
    _roles = relationship("Roles", back_populates="_users")
    _subscription_history = relationship("SubscriptionHistory", back_populates="_users")
    _messages_sender = relationship("Messages",foreign_keys="Messages.SenderId", back_populates="_users_sender")
    _messages_receiver = relationship("Messages",foreign_keys="Messages.ReceiverId", back_populates="_users_receiver")
    _offers = relationship("Offers", back_populates="_users")
    
############################################
#              Subscriptions               #
############################################
    
class SubscriptionTypes(Base):
    __tablename__ = "subscription_types"
    
    SubscriptionTypeId = Column(INTEGER, primary_key=True)
    Name = Column(VARCHAR(45), nullable=False)
    
    _subscriptions = relationship("Subscriptions", back_populates="_subscription_types")


class Subscriptions(Base):
    __tablename__ = "subscriptions"
    
    SubscriptionId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    SubscriptionTypeId = Column(INTEGER, ForeignKey("subscription_types.SubscriptionTypeId"), nullable=False)
    Name = Column(VARCHAR(45))
    DateUntil = Column(DATE, nullable=False)
    DateFrom = Column(DATE, nullable=False)
    
    _subscription_types = relationship("SubscriptionTypes", back_populates="_subscriptions")
    _subscription_history = relationship("SubscriptionHistory", back_populates="_subscriptions")

class SubscriptionHistory(Base):
    __tablename__ = "subscriptions_history"
    
    UserId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), primary_key=True)
    SubscriptionId = Column(UUID(as_uuid=True), ForeignKey("subscriptions.SubscriptionId"))
    
    _users = relationship("Users", back_populates="_subscription_history")
    _subscriptions = relationship("Subscriptions", back_populates="_subscription_history")
    
############################################
#       Subscription properties            #
############################################   
    
class PaymentStatuses(Base):
    __tablename__ = "payment_statuses"
    
    PaymentStatusId = Column(INTEGER, primary_key=True)
    PaymentStatusName = Column(VARCHAR(45))
    
    _subscription_statuses = relationship("SubscriptionStatuses", back_populates="_payment_statuses")
    
class SubscriptionStatuses(Base):
    __tablename__ = "subscription_statuses"
    
    UserId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), primary_key=True)
    PaymentStatusId = Column(INTEGER, ForeignKey("payment_statuses.PaymentStatusId"), nullable=False)
    SubscriptionId = Column(UUID(as_uuid=True), ForeignKey("subscriptions.SubscriptionId"), nullable=False)
    
    _payment_statuses = relationship("PaymentStatuses", back_populates="_subscription_statuses")
    
############################################
#                Messages                  #
############################################
    
class Messages(Base):
    __tablename__ = "messages"
    
    MessageId = Column(UUID(as_uuid=True), default=uuid4(), primary_key=True)
    SenderId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    ReceiverId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    MessageText = Column(TEXT, nullable=False)
    
    _users_sender = relationship("Users", back_populates="_messages_sender", foreign_keys=[SenderId])
    _users_receiver = relationship("Users", back_populates="_messages_receiver", foreign_keys=[ReceiverId])

############################################
#             Offer itself                 #
############################################

class Offers(Base):
    __tablename__ = "offers"
    
    OfferId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    Label = Column(VARCHAR(60), nullable=True)
    Description = Column(VARCHAR(400), nullable=True)
    PhotoPath = Column(VARCHAR(200), nullable=True)
    PublishDate = Column(DATE, nullable=True)
    ExpireDate = Column(DATE, nullable=True)
    HighPriority = Column(BOOLEAN, nullable=False)
    OwnerId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    Active = Column(BOOLEAN, nullable=False)
    
    _users = relationship("Users", back_populates="_offers")
    _offers_tags = relationship("Offers_Tags", back_populates="_offers")
    _offers_qualities = relationship("Offers_Qualities", back_populates="_offers")
    _offers_tiers = relationship("Offers_Tiers", back_populates="_offers")

############################################
#           Offer properties               #
############################################

class OfferTagGroups(Base):
    __tablename__ = "offer_tag_groups"
    
    TagGroupId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TagGroupName = Column(Enum(OfferTagGroupEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    
    _offer_tags = relationship("OfferTags", back_populates="_offer_tag_groups")
    _offers_tags = relationship("Offers_Tags", back_populates="_group_tags")

class OfferTags(Base):
    __tablename__ = "offer_tags"
    
    TagId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TagName = Column(Enum(OfferTagNamesEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    TagGroup = Column(UUID(as_uuid=True), ForeignKey("offer_tag_groups.TagGroupId"), nullable=False)
    
    _offer_tag_groups = relationship("OfferTagGroups", back_populates="_offer_tags")
    _offers_tags = relationship("Offers_Tags", back_populates="_offer_tags")
    
class OfferTiers(Base):
    __tablename__ = "offer_tiers"
    
    TierId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TierName = Column(VARCHAR(5), nullable=False)
    TierLevels = Column(ARRAY(INTEGER), nullable=True)
    
    _offers_tiers = relationship("Offers_Tiers", back_populates="_tiers")
    
class OfferQuality(Base):
    __tablename__ = "offer_qualities"
    
    QualityId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    QualityName = Column(VARCHAR(11), nullable=False)
    
    _offers_qualities = relationship("Offers_Qualities", back_populates="_quality")
    
############################################   
#         ManyToMany connections           #
############################################
    
class Offers_Tags(Base):
    __tablename__ = "offers_tags"
    
    OfferId = Column(UUID(as_uuid=True), ForeignKey("offers.OfferId"), primary_key=True)
    TagId = Column(UUID(as_uuid=True), ForeignKey("offer_tags.TagId"))
    GroupId = Column(UUID(as_uuid=True), ForeignKey("offer_tag_groups.TagGroupId"))
    
    _offer_tags = relationship("OfferTags", back_populates="_offers_tags")
    _offers = relationship("Offers", back_populates="_offers_tags")
    _group_tags = relationship("OfferTagGroups", back_populates="_offers_tags")
    
class Offers_Qualities(Base):
    __tablename__ = "offers_qualities"
    
    OfferId = Column(UUID(as_uuid=True), ForeignKey("offers.OfferId"), primary_key=True)
    QualityId = Column(UUID(as_uuid=True), ForeignKey("offer_qualities.QualityId"))
    
    _quality = relationship("OfferQuality", back_populates="_offers_qualities")
    _offers = relationship("Offers", back_populates="_offers_qualities")
    
class Offers_Tiers(Base):
    __tablename__ = "offers_tiers"
    
    OfferId = Column(UUID(as_uuid=True), ForeignKey("offers.OfferId"), primary_key=True)
    TierId = Column(UUID(as_uuid=True), ForeignKey("offer_tiers.TierId"), primary_key=True)
    
    _offers = relationship("Offers", back_populates="_offers_tiers")
    _tiers = relationship("OfferTiers", back_populates="_offers_tiers")