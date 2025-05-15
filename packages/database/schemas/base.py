from contextlib import _AsyncGeneratorContextManager
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession


class BaseSchema:
    
    @staticmethod
    async def get(session: _AsyncGeneratorContextManager[AsyncSession], id: UUID) -> "BaseSchema | None": raise NotImplementedError()
    
    async def update(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: raise NotImplementedError()
    
    async def create(self, session: _AsyncGeneratorContextManager[AsyncSession]) -> None: raise NotImplementedError()
    
    def to_dict(self) -> dict: raise NotImplementedError()