from contextlib import _AsyncGeneratorContextManager
import datetime
from typing import overload
from uuid import UUID
from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from sqlalchemy import insert, select, update

from .base import BaseSchema
from .. import models
from sqlalchemy.ext.asyncio import AsyncSession


class Offer(BaseSchema):
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def OfferId(self, v: UUID): ...
    
    @AutoProperty[str | None](access_mod=AutoPropAccessMod.Public)
    def Label(self, v: str | None): ...
    
    @AutoProperty[str | None](access_mod=AutoPropAccessMod.Public)
    def Description(self, v: str | None): ...
    
    @AutoProperty[str | None](access_mod=AutoPropAccessMod.Public)
    def PhotoPath(self, v: str | None): ...
    
    @AutoProperty[datetime.datetime | None](access_mod=AutoPropAccessMod.Public)
    def PublishDate(self, v: datetime.datetime | None): ...
    
    @AutoProperty[datetime.datetime | None](access_mod=AutoPropAccessMod.Public)
    def ExpireDate(self, v: datetime.datetime | None): ...
    
    @AutoProperty[bool](access_mod=AutoPropAccessMod.Public)
    def HighPriority(self, v: bool): ...
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def OwnerId(self, v: UUID): ...
        
    @AutoProperty[bool](access_mod=AutoPropAccessMod.Public)
    def Active(self, v: bool): ...
    
    
    
    def to_dict(self) -> dict:
        return {
            "OfferId": self.OfferId,
            "Label": self.Label,
            "Description": self.Description,
            "PhotoPath": self.PhotoPath,
            "PublishDate": self.PublishDate,
            "ExpireDate": self.ExpireDate,
            "HighPriority": self.HighPriority,
            "OwnerId": self.OwnerId,
            "Active": self.Active
        }
    
    @overload
    def __init__(
        self, 
        offer: models.Offers, 
        /
    ) -> None: ...
    
    @overload
    def __init__(
        self,
        offer,
        /,
        *, 
        label: str | None,
        description: str | None,
        photo_path: str | None,
        publish_date: datetime.datetime | None,
        expire_date: datetime.datetime | None,
        high_priority: bool | None,
        owner_id: UUID | None,
        active: bool | None
    ) -> None: ...
    
    def __init__(
        self,
        offer: models.Offers,
        /,
        *,
        label: str | None = None,
        description: str | None = None,
        photo_path: str | None = None,
        publish_date: datetime.datetime | None = None,
        expire_date: datetime.datetime | None = None,
        high_priority: bool | None = None,
        owner_id: UUID | None = None,
        active: bool | None = None
    ) -> None:
        if offer is None:
            self.Label = label
            self.Description = description
            self.PhotoPath = photo_path
            self.PublishDate = publish_date
            self.ExpireDate = expire_date
            self.HighPriority = high_priority
            self.OwnerId = owner_id
            self.Active = active
        else:
            self.Label = offer.Label
            self.Description = offer.Description
            self.PhotoPath = offer.PhotoPath
            self.PublishDate = offer.PublishDate
            self.ExpireDate = offer.ExpireDate
            self.HighPriority = offer.HighPriority
            self.OwnerId = offer.OfferId
            self.Active = offer.Active
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "Offer | None":
        async with session as s:
            result = (await s.execute(select(models.Offers).where(models.Offers.OwnerId == id))).scalar()
            
        return Offer(result) if result is not None else None

    
    async def update(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        
        updict = self.to_dict()
        
        if self.OfferId is not None:
            async with session as s:
                await s.execute(update(models.Offers).where(models.Offers.OfferId == self.OfferId).values(updict))
        else:
            raise AttributeError()
            
    
    async def create(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        
        updict = self.to_dict()
        
        if self.OfferId is not None:
            async with session as s:
                await s.execute(insert(models.Offers).values(updict))
        else:
            raise AttributeError()
        
    async def get_tags(self):
        ...
        
        
