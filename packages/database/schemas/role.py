from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from sqlalchemy import select

import packages.database.models as models
from packages.database.schemas.base import BaseSchema

from contextlib import _AsyncGeneratorContextManager
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

class Role(BaseSchema):
    
    @AutoProperty[str](access_mod=AutoPropAccessMod.Public)
    def RoleName(self, v: str | None): ...
    
    @AutoProperty[UUID](access_mod=AutoPropAccessMod.Public)
    def RoleId(self, v: UUID | None): ...
    
    @AutoProperty[int](access_mod=AutoPropAccessMod.Public)
    def RoleLevel(self, v: int | None): ...    
    
    def __init__(
        self,
        *,
        role_id: UUID | None = None,
        role_name: str | None = None,
        role_level: int | None = None,
    ) -> None :
        
        self.RoleId = role_id
        self.RoleName = role_name
        self.RoleLevel = role_level
    
    @classmethod
    def from_model(cls, user: models.Roles) -> "Role":
        self = cls()
        
        self.RoleId = user.RoleId
        self.RoleName = user.RoleName
        self.RoleLevel = user.RoleLevel
        
        return self
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "Role | None": 
        async with session as s:
            result = (await s.execute(select(models.Roles).where(models.Roles.RoleId == id))).scalar()
            
        return Role.from_model(result) if result is not None else None
    
    def to_dict(self) -> dict:
        return {
            "RoleId" : self.RoleId,
            "RoleName" : self.RoleName,
            "RoleLevel" : self.RoleLevel
        }