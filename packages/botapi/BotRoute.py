

from typing import Iterable, Callable

from telebot.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup

from telebot.states import State

from telebot.states.asyncio.context import StateContext  # type: ignore

from packages.botapi.StateController import StateController
from packages.botmaster import BotMaster
from packages.intefraces.IBotMaster import IBotMaster

from telebot.async_telebot import AsyncTeleBot

import telebot

from packages.intefraces.IStateController import IStateController
from packages.validator import AutoProperty


class BaseBotRoute:
    

    @AutoProperty(IStateController | None)
    def StateControl(self) -> IStateController | None: ...
    
    @AutoProperty(Message | None)
    def UsersMessage(self) -> Message | None: ...
    
    @AutoProperty(IBotMaster | None)
    def Botmas(self) -> IBotMaster | None: ...
    
    @AutoProperty(Iterable[str])
    def Commands(self) -> Iterable[str]: ...
    
    @AutoProperty(Iterable[str])
    def ContentTypes(self) -> Iterable[str]: ...
    
    @AutoProperty(str | None)
    def Regexp(self) -> str | None: ...
    
    @AutoProperty(Callable | None)
    def Func(self) -> Callable | None: ...
    
    @AutoProperty(State | str | None)
    def StatmentState(self) -> State | str | None: ...
    
    @AutoProperty(bool | None)
    def IsDigit(self) -> bool | None: ...

    @AutoProperty(ReplyKeyboardMarkup | InlineKeyboardMarkup | None)
    def Keyboard(self) -> ReplyKeyboardMarkup | InlineKeyboardMarkup | None: ...

    @AutoProperty(str)
    def UserId(self) -> str: ...

    async def __call__(self, message: telebot.types.Message, state: StateContext, bot: AsyncTeleBot):
        self.Botmas = BotMaster(bot)
        self.UsersMessage = message
        self.StateControl = StateController(state)
        if self.UsersMessage is not None:
            self._user_id: str = str(self.UsersMessage.chat)

    async def Endpoint(self) -> None:
        raise NotImplementedError()

