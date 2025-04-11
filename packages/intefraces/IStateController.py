from typing import Protocol, Union
from telebot.states import State

from telebot.states.asyncio.context import StateContext

class IStateController(Protocol):
    
    _context_state: StateContext

    @property
    def ContextState(self) -> StateContext:
        ...
        
    @ContextState.setter
    def ContextState(self, state: StateContext) -> None:
        ...
        
    async def SetNextState(self, state: Union[State, str]) -> None:
        ...

    async def AddDataState(self, **kwargs) -> None:
        ...

    async def GetDataState(self) -> dict:
        ...

    async def ResetStates(self) -> None:
        ...