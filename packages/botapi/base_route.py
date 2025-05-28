

from contextlib import _AsyncGeneratorContextManager
from typing import Any, Iterable, Callable

from telebot.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup

from telebot.states import State

from telebot.states.asyncio.context import StateContext  # type: ignore

from packages.botapi.state_controller import StateController
from packages.botmaster import BotMaster
from packages.database import get_session
from packages.intefraces.IBotMaster import IBotMaster

from telebot.async_telebot import AsyncTeleBot

import telebot

from autoproperty import AutoProperty

from sqlalchemy.ext.asyncio import AsyncSession


class BaseBotRoute:

    @AutoProperty[StateController](annotationType=StateController | None, access_mod="protected")
    def StateControl(self): ...

    @AutoProperty[Message](annotationType=Message | None, access_mod="public", s_access_mod="protected")
    def UsersMessage(self) -> Message | None: ...

    @AutoProperty[IBotMaster](annotationType=IBotMaster | None, access_mod="public", s_access_mod="protected")
    def Botmas(self) -> IBotMaster | None: ...

    @AutoProperty[list[str]](annotationType=list | tuple, access_mod="public", s_access_mod="protected")
    def Commands(self) -> list[str]: ...

    @AutoProperty[list[str]](annotationType=list | tuple, access_mod="public", s_access_mod="protected")
    def ContentTypes(self) -> list[str]: ...

    @AutoProperty[str | None](annotationType=str | None, access_mod="public", s_access_mod="protected")
    def Regexp(self) -> str | None: ...

    @AutoProperty[Callable | None](annotationType=object, access_mod="public", s_access_mod="protected")
    def Func(self) -> Callable | None: ...

    @AutoProperty[State | str | None](annotationType=State | str | None, access_mod="public", s_access_mod="protected")
    def StatmentState(self) -> State | str | None: ...

    @AutoProperty[bool | None](annotationType=bool | None, access_mod="public", s_access_mod="protected")
    def IsDigit(self) -> bool | None: ...

    @AutoProperty[ReplyKeyboardMarkup | InlineKeyboardMarkup | None](annotationType=ReplyKeyboardMarkup | InlineKeyboardMarkup | None, access_mod="public", s_access_mod="protected")
    def Keyboard(self) -> ReplyKeyboardMarkup | InlineKeyboardMarkup | None: ...

    @AutoProperty[int](annotationType=int, access_mod="public", s_access_mod="protected")
    def UserId(self) -> int: ...

    @property
    def Session(self): 
        return get_session()

    def __init__(self) -> None:
        ...

    async def __call__(self, message: telebot.types.Message, state: StateContext, bot: AsyncTeleBot) -> None:
        self.Botmas = BotMaster(bot)
        self.UsersMessage = message
        self.StateControl = StateController(state)
        if self.UsersMessage is not None:
            self.UserId = self.UsersMessage.chat.id
