from uuid import uuid4
from sqlalchemy import BIGINT, BOOLEAN, DATE, INTEGER, NVARCHAR, TEXT, Column, ForeignKey
from .base import Base
from sqlalchemy.dialects.postgresql import UUID


class Roles(Base):
    __tablename__ = "roles"
    
    RoleId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    RoleName = Column(NVARCHAR(50), nullable=False)
    RoleLevel = Column(INTEGER, nullable=False)

class Users(Base):
    __tablename__ = "users"
    
    UserId = Column(UUID(as_uuid=True),primary_key=True, default=uuid4())
    PhoneNumber = Column(NVARCHAR(11), nullable=True)
    TelegramId = Column(BIGINT, nullable=False)
    IsVip = Column(BOOLEAN, nullable=False)
    role = Column(UUID(as_uuid=True), ForeignKey("roles.RoleId"), nullable=False)
    
class SubscriptionTypes(Base):
    __tablename__ = "subscription_types"
    
    SubscriptionTypeId = Column(INTEGER, primary_key=True)
    Name = Column(NVARCHAR(45), nullable=False)

class Subscriptions(Base):
    __tablename__ = "subscriptions"
    
    SubscriptionId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    SubscriptionTypeId = Column(INTEGER, ForeignKey("subscription_types.SubscriptionTypeId"), nullable=False)
    Name = Column(NVARCHAR(45))
    DateUntil = Column(DATE, nullable=False)
    DateFrom = Column(DATE, nullable=False)

class SubscriptionHistory(Base):
    __tablename__ = "subscriptions_history"
    
    UserId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), primary_key=True)
    SubscriptionId = Column(UUID(as_uuid=True), ForeignKey("subscriptions.SubscriptionId"))
    
class PaymentStatuses(Base):
    __tablename__ = "payment_statuses"
    
    PaymentStatusId = Column(INTEGER, primary_key=True)
    PaymentStatusName = Column(NVARCHAR(45))
    
class Subscription_Statuses(Base):
    __tablename__ = "subscription_statuses"
    
    UserId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), primary_key=True)
    PaymentStatusId = Column(INTEGER, ForeignKey("payment_statuses.PaymentStatusId"), nullable=False)
    SubscriptionId = Column(UUID(as_uuid=True), ForeignKey("subscriptions.SubscriptionId"), nullable=False)
    
class Messages(Base):
    __tablename__ = "messages"
    
    MessageId = Column(UUID(as_uuid=True), default=uuid4(), primary_key=True)
    SenderId = Column(UUID(as_uuid=True), ForeignKey(), nullable=False)
    ReceiverId = Column(UUID(as_uuid=True), ForeignKey(), nullable=False)
    MessageText = Column(TEXT, nullable=False)
    
class Offers(Base):
    __tablename__ = "offers"
    
    OfferId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    Label = Column(NVARCHAR(60), nullable=True)
    Description = Column(NVARCHAR(400), nullable=True)
    PhotoPath = Column(NVARCHAR(200), nullable=True)
    PublishDate = Column(DATE, nullable=True)
    ExpireDate = Column(DATE, nullable=True)
    HighPriority = Column(BOOLEAN, nullable=False)
    OwnerId = Column(UUID(as_uuid=True), ForeignKey("users.UserId"), nullable=False)
    Active = Column(BOOLEAN, nullable=False)

class OfferTagGroups(Base):
    __tablename__ = "offer_tag_groups"
    
    TagGroupId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TagGroupName = Column(NVARCHAR(60), nullable=False)

class OfferTags(Base):
    __tablename__ = "offer_tags"
    
    TagId = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    TagName = Column(NVARCHAR(60), nullable=False)
    TagGroup = Column(UUID(as_uuid=True), ForeignKey("offer_tag_groups.TagGroupId"), nullable=False)