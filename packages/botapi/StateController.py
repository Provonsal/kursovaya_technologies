from typing import Union
from telebot.states import State
from telebot.asyncio_storage.base_storage import StateDataContext

from telebot.states.asyncio.context import StateContext

class StateController:
    _context_state: StateContext
    
    def __init__(self, contextState: StateContext) -> None:
        self.ContextState = contextState

    @property
    def ContextState(self) -> StateContext:
        return self._context_state
        
    @ContextState.setter
    def ContextState(self, state: StateContext) -> None:
        self._context_state = state
        
    async def SetNextState(self, state: Union[State, str]) -> None:
        await self._context_state.set(state)

    async def AddDataState(self, **kwargs) -> None:
        await self._context_state.add_data(**kwargs)

    async def GetDataState(self) -> dict:
        
        async with self._context_state.data() as data:  # type: ignore
            return data

    async def ResetStates(self) -> None:
        await self._context_state.delete()