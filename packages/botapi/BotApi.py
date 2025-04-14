from contextlib import _AsyncGeneratorContextManager
from telebot.async_telebot import AsyncTeleBot # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Callable, Protocol

from packages.intefraces.IBotMaster import IBotMaster

class BotApi:
    
    _bot: AsyncTeleBot
    _botMaster: IBotMaster
    
    @property
    def Bot(self) -> AsyncTeleBot:
        ...
        
    @Bot.setter
    def Bot(self, bot: AsyncTeleBot) -> None:
        ...
        
    @property
    def BotMaster(self) -> IBotMaster:
        ...
    
    @BotMaster.setter
    def BotMaster(self, botMaster: IBotMaster) -> None:
        ...
    
    @property
    def Session(self) -> _AsyncGeneratorContextManager[AsyncSession, None]:
        ...

    @Session.setter
    def Session(self, session: AsyncSession) -> None:
        ...
    
    def __iadd__(self, handler) -> "BotApi":
        ...
    
    def Poll(self) -> None:
        ...
        
    def AddHandlers(self, handlers: list[Callable]) -> None:
        ...