

from types import NoneType
from typing import Iterable, Optional, Union, Callable

from telebot.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup

from telebot.states import State

from telebot.states.asyncio.context import StateContext  # type: ignore

from packages.botapi.StateController import StateController
from packages.botmaster import BotMaster
from packages.intefraces.IBotMaster import IBotMaster

from telebot.async_telebot import AsyncTeleBot

import telebot

from packages.intefraces.IStateController import IStateController
from packages.validator import FieldValidator


class BaseBotRoute:
    # Fields that is empty on default and filling only when handler got triggered
    _message: Message | None
    _botmas: IBotMaster | None
    _stateController: IStateController | None

    # Fields for handling needed situations while
    # interacting with user
    _commands: Iterable[str]
    _content_ypes: Iterable[str]
    _regexp: str | None
    _func: Callable | None
    _statment_state: State | str | None
    _is_digit: bool | None

    # Variables for developer's comfort.
    _keyboard: ReplyKeyboardMarkup | InlineKeyboardMarkup | None
    _user_id: str

    @property
    def StateControl(self) -> IStateController | None:
        return self._stateController

    @property
    def UsersMessage(self) -> Message | None:
        return self._message

    @property
    def Botmas(self) -> IBotMaster | None:
        return self._botmas

    @property
    def Commands(self) -> Iterable[str]:
        return self._commands

    @property
    def ContentTypes(self) -> Iterable[str]:
        return self._content_ypes

    @property
    def Regexp(self) -> str | None:
        return self._regexp

    @property
    def Func(self) -> Callable | None:
        return self._func

    @property
    def StatmentState(self) -> State | str | None:
        return self._statment_state

    @property
    def IsDigit(self) -> bool | None:
        return self._is_digit

    @property
    def Keyboard(self) -> ReplyKeyboardMarkup | InlineKeyboardMarkup | None:
        return self._keyboard

    @property
    def UserId(self) -> str:
        return self._user_id

    @StateControl.setter
    @FieldValidator("_stateController", IStateController)
    def StateControl(self, stateController: IStateController):
        self._stateController = stateController

    @UsersMessage.setter
    @FieldValidator("_message", telebot.types.Message | None)
    def UsersMessage(self, message: telebot.types.Message | None) -> None:

        self._message = message

    @Botmas.setter
    @FieldValidator("_botmas", IBotMaster | None)
    def Botmas(self, botmas: IBotMaster | None) -> None:

        self._botmas = botmas

    @Commands.setter
    @FieldValidator("_commands", Iterable[str])
    def Commands(self, commands: Iterable[str]) -> None:

        self._commands = commands

    @ContentTypes.setter
    @FieldValidator("_contenTypes", Iterable[str])
    def ContentTypes(self, contenTypes: Iterable[str]) -> None:

        self._contenTypes = contenTypes

    @Regexp.setter
    @FieldValidator("_regexp", str)
    def Regexp(self, regexp: str) -> None:

        self._regexp = regexp

    @Func.setter
    @FieldValidator("_func", Callable | None)
    def Func(self, func: Callable | None) -> None:

        self._func = func

    @StatmentState.setter
    @FieldValidator("_state", State | str | None)
    def StatmentState(self, state: State | str | None) -> None:

        self._state = state

    @IsDigit.setter
    @FieldValidator("_is_digit", bool | None)
    def IsDigit(self, isDigit: bool | None) -> None:

        self._is_digit = isDigit

    @Keyboard.setter
    @FieldValidator("_keyboard", ReplyKeyboardMarkup | InlineKeyboardMarkup | None)
    def Keyboard(self, keyboard: ReplyKeyboardMarkup | InlineKeyboardMarkup | None) -> None:

        self._keyboard = keyboard

    @UserId.setter
    @FieldValidator("user_id", str)
    def UserId(self, user_id: str) -> None:

        self._user_id = user_id

    async def __call__(self, message: telebot.types.Message, state: StateContext, bot: AsyncTeleBot):
        self.Botmas = BotMaster(bot)
        self.UsersMessage = message
        self.StateControl = StateController(state)
        if self.UsersMessage is not None:
            self._user_id: str = str(self.UsersMessage.chat)

    async def Endpoint(self) -> None:
        raise NotImplementedError()
