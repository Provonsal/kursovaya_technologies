from typing import Optional
from telebot.async_telebot import AsyncTeleBot  # type: ignore


from telebot.states.asyncio.middleware import StateMiddleware  # type: ignore
from telebot import asyncio_filters  # type: ignore

from telebot.types import InlineKeyboardMarkup  # type: ignore
from autoproperty import AutoProperty


class BotMaster():

    def __init__(self, bot: AsyncTeleBot) -> None:
        self.Bot = bot

    @AutoProperty[AsyncTeleBot](annotationType=AsyncTeleBot, access_mod="public", s_access_mod="private")
    def Bot(self): ...

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
