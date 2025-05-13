from typing import Union
from telebot.states import State
from autoproperty import AutoProperty

from telebot.states.asyncio.context import StateContext

class StateController:
    __contextState: StateContext
    
    def __init__(self, contextState: StateContext) -> None:
        self.ContextState = contextState
        
    @AutoProperty[StateContext]
    def ContextState(self): ...
        
    async def SetNextState(self, state: Union[State, str]) -> None:
        await self.__contextState.set(state)

    async def AddDataState(self, **kwargs) -> None:
        await self.__contextState.add_data(**kwargs)

    async def GetDataState(self) -> dict:
        
        async with self.__contextState.data() as data:  # type: ignore
            return data

    async def ResetStates(self) -> None:
        await self.__contextState.delete()