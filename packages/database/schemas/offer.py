from contextlib import _AsyncGeneratorContextManager
import datetime
from uuid import UUID
from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from sqlalchemy import Result, insert, select, update

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
    
    @AutoProperty[list](access_mod=AutoPropAccessMod.Public)
    def Tags(self, v: list): ...
    
    @AutoProperty[list](access_mod=AutoPropAccessMod.Public)
    def Tiers(self, v: list): ...
    
    @AutoProperty[list](access_mod=AutoPropAccessMod.Public)
    def Qualities(self, v: list): ...
    
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
    
    def __init__(
        self,
        *,
        tags: list | tuple, 
        tiers: list | tuple, 
        qualities: list | tuple,
        label: str | None = None,
        description: str | None = None,
        photo_path: str | None = None,
        publish_date: datetime.datetime | None = None,
        expire_date: datetime.datetime | None = None,
        high_priority: bool | None = None,
        owner_id: UUID | None = None,
        active: bool | None = None
    ) -> None:

        self.Label = label
        self.Description = description
        self.PhotoPath = photo_path
        self.PublishDate = publish_date
        self.ExpireDate = expire_date
        self.HighPriority = high_priority
        self.OwnerId = owner_id
        self.Active = active
        self.Tags = tags
        self.Tiers = tiers
        self.Qualities = qualities

    
    @classmethod
    def from_model(cls, offer: models.Offers, tags: list | tuple, tiers: list | tuple, qualities: list | tuple) -> "Offer":
        self = cls(
            tags=tags,
            tiers=tiers,
            qualities=qualities
        )
        
        self.Label = offer.Label
        self.Description = offer.Description
        self.PhotoPath = offer.PhotoPath
        self.PublishDate = offer.PublishDate
        self.ExpireDate = offer.ExpireDate
        self.HighPriority = offer.HighPriority
        self.OwnerId = offer.OfferId
        self.Active = offer.Active
        
        return self
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "Offer | None":
        async with session as s:
            result = (await s.execute(select(models.Offers).where(models.Offers.OwnerId == id))).scalar()
            if result is not None:
                tags_ids: Result = await s.execute(select(models.Offers_Tags.TagId).where(models.Offers_Tiers.OfferId == result.OfferId))
                tags = tuple((await s.execute(select(models.Roles.RoleName).where(models.Roles.RoleId.in_(tags_ids.scalars().all())))).scalars().all())
                
                tiers_ids = await s.execute(select(models.Offers_Tiers.TierId).where(models.Offers_Tiers.OfferId == result.OfferId))
                tiers = tuple((await s.execute(select(models.OfferTiers.TierName).where(models.OfferTiers.TierId.in_(tiers_ids.scalars().all())))).scalars().all())
                
                qualities_ids = await s.execute(select(models.Offers_Qualities.QualityId).where(models.Offers_Qualities.OfferId == result.OfferId))
                qualities = tuple((await s.execute(select(models.OfferQuality.QualityName).where(models.OfferQuality.QualityId.in_(qualities_ids.scalars().all())))).scalars().all())
        
            
        return Offer.from_model(result, tags, tiers, qualities) if result is not None else None

    
    async def update(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        
        if self.OfferId is not None:
            async with session as s:
                await s.execute(update(models.Offers).where(models.Offers.OfferId == self.OfferId).values(self.to_dict()))
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
        
        
