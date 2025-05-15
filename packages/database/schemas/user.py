import datetime
from typing import overload
from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from sqlalchemy import insert, select, update

import models
from schemas.base import BaseSchema

from contextlib import _AsyncGeneratorContextManager
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

class User(BaseSchema):
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def UserId(self, v: UUID): ...
    
    @AutoProperty[str](access_mod=AutoPropAccessMod.Public)
    def PhoneNumber(self, v: str): ...
    
    @AutoProperty[str](access_mod=AutoPropAccessMod.Public)
    def TelegramId(self, v: str): ...
    
    @AutoProperty[bool](access_mod=AutoPropAccessMod.Public)
    def IsVip(self, v: bool): ...
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def RoleId(self, v: UUID): ...
    
    @overload
    def __init__(
        self, 
        user: models.Users, 
        /
    ) -> None: ...
    
    @overload
    def __init__(
        self,
        user,
        /,
        *, 
        user_id: UUID | None,
        phone_number: str | None,
        telegram_id: str | None,
        is_vip: bool| None,
        role_id: UUID | None
    ) -> None: ...
    
    def __init__(
        self,
        user: models.Users,
        /,
        *,
        user_id: UUID | None = None,
        phone_number: str | None = None,
        telegram_id: str | None = None,
        is_vip: bool| None = None,
        role_id: UUID | None = None
    ) -> None :
        if user is None:
            self.UserId = user_id
            self.PhoneNumber = phone_number
            self.TelegramId = telegram_id
            self.IsVip = is_vip
            self.RoleId = role_id
        else:
            self.UserId = user.UserId
            self.PhoneNumber = user.PhoneNumber
            self.TelegramId = user.TelegramId
            self.IsVip = user.IsVip
            self.RoleId = user.RoleId
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "User | None": 
        async with session as s:
            result = (await s.execute(select(models.Users).where(models.Users.UserId == id))).scalar()
            
        return User(result) if result is not None else None
    
    @staticmethod
    async def get_by_telegramId(session: _AsyncGeneratorContextManager[AsyncSession], telegram_id: str) -> "User | None":
        async with session as s:
            result = (await s.execute(select(models.Users).where(models.Users.TelegramId == telegram_id))).scalar()
            
        return User(result) if result is not None else None
    
    async def update(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        updict = self.to_dict()
        
        if self.UserId is not None:
            async with session as s:
                await s.execute(update(models.Users).where(models.Users.UserId == self.UserId).values(updict))
        else:
            raise AttributeError()
    
    async def create(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: 
        updict = self.to_dict()
        
        if self.UserId is not None:
            async with session as s:
                await s.execute(insert(models.Users).values(updict))
        else:
            raise AttributeError()
    
    def to_dict(self) -> dict:
        return {
            "UserId" : self.UserId,
            "PhoneNumber" : self.PhoneNumber,
            "TelegramId" : self.TelegramId,
            "IsVip" : self.IsVip,
            "RoleId" : self.RoleId
        }