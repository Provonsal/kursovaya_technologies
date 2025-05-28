import datetime
from typing import overload
from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from sqlalchemy import Result, select, update, exists
from sqlalchemy.dialects.postgresql import insert

import packages.database.models as models
from packages.database.schemas.base import BaseSchema

from contextlib import _AsyncGeneratorContextManager
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

class User(BaseSchema):
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def UserId(self, v: UUID | None): ...
    
    @AutoProperty[str](access_mod=AutoPropAccessMod.Public)
    def PhoneNumber(self, v: str | None): ...
    
    @AutoProperty[int](access_mod=AutoPropAccessMod.Public)
    def TelegramId(self, v: int | None): ...
    
    @AutoProperty[bool](access_mod=AutoPropAccessMod.Public)
    def IsVip(self, v: bool | None): ...
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def RoleId(self, v: UUID | None): ...
    
    def __init__(
        self,
        *,
        user_id: UUID | None = None,
        phone_number: str | None = None,
        telegram_id: int | None = None,
        is_vip: bool | None = None,
        role_id: UUID | None = None
    ) -> None :
        
        self.UserId = user_id
        self.PhoneNumber = phone_number
        self.TelegramId = telegram_id
        self.IsVip = is_vip if is_vip is not None else False
        self.RoleId = role_id
    
    @classmethod
    def from_model(cls, user: models.Users) -> "User":
        self = cls()
        
        self.UserId = user.UserId
        self.PhoneNumber = user.PhoneNumber
        self.TelegramId = user.TelegramId
        self.IsVip = user.IsVip
        self.RoleId = user.RoleId
        
        return self
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "User | None": 
        async with session as s:
            result = (await s.execute(select(models.Users).where(models.Users.UserId == id))).scalar()
            
        return User.from_model(result) if result is not None else None
    
    @staticmethod
    async def get_by_telegramId(session: _AsyncGeneratorContextManager[AsyncSession], telegram_id: int) -> "User | None":
        async with session as s:
            result = (await s.execute(select(models.Users).where(models.Users.TelegramId == telegram_id))).scalar()
            
        return User.from_model(result) if result is not None else None
    
    async def update(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        updict = self.to_dict()
        
        if self.UserId is not None:
            async with session as s:
                await s.execute(update(models.Users).where(models.Users.UserId == self.UserId).values(updict))
        else:
            raise AttributeError()
    
    async def create(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        if self.UserId is not None:
            async with session as s:
                if self.RoleId is None:
                    stmt = select(models.Roles.RoleId).where(models.Roles.RoleName == "user")
                    result = (await s.execute(stmt)).scalar()
                  
                    if result is not None:
                        self.RoleId = result
                    else:
                        raise Exception("Role id not found")
                
                stmt2 = insert(models.Users).values(self.to_dict()).on_conflict_do_nothing()
                await s.execute(stmt2)
        else:
            raise AttributeError(name="debug")
    
    def to_dict(self) -> dict:
        return {
            "UserId" : self.UserId,
            "PhoneNumber" : self.PhoneNumber,
            "TelegramId" : self.TelegramId,
            "IsVip" : self.IsVip,
            "RoleId" : self.RoleId
        }