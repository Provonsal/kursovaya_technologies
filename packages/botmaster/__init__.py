from telebot.async_telebot import AsyncTeleBot # type: ignore

from env import Config

from telebot.states.asyncio.middleware import StateMiddleware # type: ignore
from telebot import asyncio_filters # type: ignore
from telebot.asyncio_storage import StateRedisStorage

from telebot.types import InlineKeyboardMarkup # type: ignore

class BotMaster:
    
    _bot: AsyncTeleBot
    
    @property
    def Bot(self) -> AsyncTeleBot:
        return self._bot
        
    @Bot.setter
    def Bot(self, bot: AsyncTeleBot) -> None:
        if isinstance(bot, AsyncTeleBot):
            self._bot = bot
        else:
            raise Exception("Wrong bot type")
        
    
    def __init__(self, bot: AsyncTeleBot | None) -> None:
        self._bot: AsyncTeleBot = bot if bot is not None else AsyncTeleBot(Config.GetValue("TOKEN"), state_storage=StateRedisStorage())
    
    async def Poll(self) -> None:
        # включаем какую то штуку
        self._bot.setup_middleware(StateMiddleware(self._bot))
        
        # добавляем кастомные фильтры для цифр и для того чтобы работали "состояния пользователей"
        self._bot.add_custom_filter(asyncio_filters.StateFilter(self._bot))
        self._bot.add_custom_filter(asyncio_filters.IsDigitFilter())
        
        # запускаем поллинг
        await self._bot.polling()
    
    async def SendMessage(self, user_id: int, message: str, reply_markup: InlineKeyboardMarkup | None) -> None:
        if reply_markup is not None:
            await self._bot.send_message(user_id, message, reply_markup=reply_markup)
        else:
            await self._bot.send_message(user_id, message)