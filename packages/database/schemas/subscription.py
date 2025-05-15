from contextlib import _AsyncGeneratorContextManager
import datetime
from typing import overload
from uuid import UUID
from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

import models
from schemas.base import BaseSchema


class Subscription(BaseSchema):
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def SubscriptionId(self, v: UUID): ...
    
    @AutoProperty[int](access_mod=AutoPropAccessMod.Public)
    def SubscriptionTypeId(self, v: int): ...
    
    @AutoProperty[str](access_mod=AutoPropAccessMod.Public)
    def Name(self, v: str): ...
    
    @AutoProperty[datetime.datetime](access_mod=AutoPropAccessMod.Public)
    def DateUntil(self, v: datetime.datetime): ...
    
    @AutoProperty[datetime.datetime](access_mod=AutoPropAccessMod.Public)
    def DateFrom(self, v: datetime.datetime): ...
    
    @overload
    def __init__(
        self, 
        subscription: models.Subscriptions, 
        /
    ) -> None: ...
    
    @overload
    def __init__(
        self,
        subscription: models.Subscriptions,
        /,
        *, 
        subscription_id: UUID | None,
        subscription_type_id: int | None,
        name: str | None,
        date_until: datetime.datetime | None,
        date_from: datetime.datetime | None
    ) -> None: ...
    
    def __init__(
        self,
        subscription: models.Subscriptions,
        /,
        *, 
        subscription_id: UUID | None = None,
        subscription_type_id: int | None = None,
        name: str | None = None,
        date_until: datetime.datetime | None = None,
        date_from: datetime.datetime | None = None
    ) -> None:
        if subscription is None:
            self.SubscriptionId = subscription_id
            self.SubscriptionTypeId = subscription_type_id
            self.Name = name
            self.DateUntil = date_until
            self.DateFrom = date_from
        else:
            self.SubscriptionId = subscription.SubscriptionId
            self.SubscriptionTypeId = subscription.SubscriptionTypeId
            self.Name = subscription.Name
            self.DateUntil = subscription.DateUntil
            self.DateFrom = subscription.DateFrom
    
    def to_dict(self) -> dict:
        return super().to_dict()
    
    async def create(self, session: _AsyncGeneratorContextManager[AsyncSession, None]) -> None:
        updict = self.to_dict()
        
        if self.SubscriptionId is not None:
            async with session as s:
                await s.execute(insert(models.Subscriptions).values(updict))
        else:
            raise AttributeError()
    
    async def update(self, session: _AsyncGeneratorContextManager[AsyncSession, None]) -> None:
        updict = self.to_dict()
        
        if self.SubscriptionId is not None:
            async with session as s:
                await s.execute(update(models.Subscriptions).where(models.Subscriptions.SubscriptionId == self.SubscriptionId).values(updict))
        else:
            raise AttributeError()
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "BaseSchema | None":
        async with session as s:
            result = (await s.execute(select(models.Subscriptions).where(models.Subscriptions.SubscriptionId == id))).scalar()
            
        return Subscription(result) if result is not None else None
    
    