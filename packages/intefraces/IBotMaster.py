from telebot.types import InlineKeyboardMarkup # type: ignore
from telebot.async_telebot import AsyncTeleBot # type: ignore

from typing import Optional, Protocol, runtime_checkable

@runtime_checkable
class IBotMaster(Protocol):
    
    @property
    def Bot(self) -> AsyncTeleBot:
        ...
        
    @Bot.setter
    def Bot(self, bot: AsyncTeleBot) -> None:
        ...
    
    async def Poll(self) -> None:
        ...
    
    async def SendMessage(self, user_id: int, message: str, reply_markup: Optional[InlineKeyboardMarkup]) -> None:
        ...
    