from typing import Union
from telebot.states import State
from autoproperty import AutoProperty

from telebot.states import asyncio, sync

class StateController:
    __contextState: asyncio.context.StateContext
    
    def __init__(self, contextState: asyncio.context.StateContext) -> None:
        self.ContextState = contextState
        
    @AutoProperty[asyncio.context.StateContext](access_mod="public")
    def ContextState(self, v: asyncio.context.StateContext | sync.context.StateContext): ...
        
    async def SetNextState(self, state: Union[State, str]) -> None:
        await self.ContextState.set(state)

    async def AddDataState(self, **kwargs) -> None:
        await self.ContextState.add_data(**kwargs)

    async def GetDataState(self) -> dict:
        async with self.ContextState.data() as data:  # type: ignore
            return data

    async def ResetStates(self) -> None:
        await self.ContextState.delete()