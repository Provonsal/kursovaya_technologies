from telebot.types import InlineKeyboardMarkup # type: ignore
from telebot.async_telebot import AsyncTeleBot # type: ignore

from typing import Optional

from packages.validator import FieldValidator

from telebot.states.asyncio.middleware import StateMiddleware # type: ignore
from telebot import asyncio_filters
from telebot.async_telebot import AsyncTeleBot

class BotMaster():
    
    _bot: AsyncTeleBot
    
    def __init__(self, bot: AsyncTeleBot) -> None:
        self.Bot = bot
    
    @property
    def Bot(self) -> AsyncTeleBot:
        return self._bot
        
    @Bot.setter
    @FieldValidator("_bot", AsyncTeleBot)
    def Bot(self, bot: AsyncTeleBot) -> None:
        self._bot = bot
    
    async def Poll(self) -> None:
        # включаем какую то штуку
        self.Bot.setup_middleware(StateMiddleware(self.Bot))
        
        # добавляем кастомные фильтры для цифр и для того чтобы работали "состояния пользователей"
        self.Bot.add_custom_filter(asyncio_filters.StateFilter(self.Bot))
        self.Bot.add_custom_filter(asyncio_filters.IsDigitFilter())
        
        # запускаем поллинг
        await self.Bot.polling()
    
    async def SendMessage(self, user_id: int, message: str, reply_markup: Optional[InlineKeyboardMarkup]) -> None:
        if reply_markup is not None:
            await self.Bot.send_message(user_id, message, reply_markup=reply_markup)
        else:
            await self.Bot.send_message(user_id, message)