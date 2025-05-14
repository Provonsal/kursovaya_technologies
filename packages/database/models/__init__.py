from uuid import uuid4
from sqlalchemy import BIGINT, BOOLEAN, DATE, INTEGER, VARCHAR, TEXT, Column, ForeignKey
from .base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


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
    TelegramId = Column(BIGINT, nullable=False)
    IsVip = Column(BOOLEAN, nullable=False)
    role = Column(UUID(as_uuid=True), ForeignKey("roles.RoleId"), nullable=False)
    
    _roles = relationship("Roles", back_populates="_users")
    _subscription_history = relationship("SubscriptionHistory", back_populates="_subscriptions")
    _messages = relationship("Messages", "_users")
    _offers = relationship("Offers", back_populates="_users")
    
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
    _subscriptions = relationship("Subscriptions", back_populates="")
    
    
    
    
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
    
class Messages(Base):
    __tablename__ = "messages"
    
    MessageId = Column(UUID(as_uuid=True), default=uuid4(), primary_key=True)
    SenderId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    ReceiverId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    MessageText = Column(TEXT, nullable=False)
    
    _users = relationship("Users", back_populates="_messages")
    
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

class OfferTagGroups(Base):
    __tablename__ = "offer_tag_groups"
    
    TagGroupId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TagGroupName = Column(VARCHAR(60), nullable=False)
    
    _offer_tags = relationship("OfferTags", back_populates="_offer_tag_groups")
    _offers_tags = relationship("Offers_Tags", back_populates="_group_tags")

class OfferTags(Base):
    __tablename__ = "offer_tags"
    
    TagId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TagName = Column(VARCHAR(60), nullable=False)
    TagGroup = Column(UUID(as_uuid=True), ForeignKey("offer_tag_groups.TagGroupId"), nullable=False)
    
    _offer_tag_groups = relationship("OfferTagGroups", back_populates="_offer_tags")
    
class Offers_Tags(Base):
    __tablename__ = "offers_tags"
    
    OfferId = Column(UUID(as_uuid=True), ForeignKey("offers.OfferId"), primary_key=True)
    TagId = Column(UUID(as_uuid=True), ForeignKey("offer_tags.TagId"))
    GroupId = Column(UUID(as_uuid=True), ForeignKey("offer_tag_groups.TagGroupId"))
    
    _offer_tags = relationship("OfferTags", back_populates="_offer_tag_groups")
    _offers = relationship("Offers", back_populates="_offers_tags")
    _group_tags = relationship("OfferTagGroup", back_populates="_offers_tags")