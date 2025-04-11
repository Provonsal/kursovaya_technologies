

from typing import Iterable, Protocol, Optional, Union, Callable

from telebot.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup

from telebot.states import State

from telebot.states.asyncio.context import StateContext

from packages.intefraces.IBotMaster import IBotMaster

from telebot.async_telebot import AsyncTeleBot

import telebot

from packages.intefraces.IStateController import IStateController


class IBotApiRoute(Protocol):

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
    def Message(self) -> Message | None:
        ...

    @property
    def Botmas(self) -> IBotMaster | None:
        ...

    @property
    def Commands(self) -> list:
        ...

    @property
    def ContentTypes(self) -> list:
        ...

    @property
    def Regexp(self) -> Optional["str"]:
        ...

    @property
    def Func(self) -> Optional[Callable]:
        ...

    @property
    def StatmentState(self) -> Optional[Union["State", "str"]]:
        ...

    @property
    def IsDigit(self) -> Optional[bool]:
        ...

    @property
    def Keyboard(self) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
        ...

    @property
    def UserId(self) -> str:
        ...

    @Message.setter
    def Message(self, message: telebot.types.Message | None) -> None:
        ...

    @Botmas.setter
    def Botmas(self, botmas: IBotMaster | None) -> None:
        ...

    @Commands.setter
    def Commands(self, commands: Iterable[str]) -> None:
        ...

    @ContentTypes.setter
    def ContentTypes(self, contenTypes: Iterable[str]) -> None:
        ...

    @Regexp.setter
    def Regexp(self, regexp: str) -> None:
        ...

    @Func.setter
    def Func(self, func: Callable | None) -> None:
        ...

    @StatmentState.setter
    def StatmentState(self, state: State | str | None) -> None:
        ...

    @IsDigit.setter
    def IsDigit(self, isDigit: bool | None) -> None:
        ...

    @Keyboard.setter
    def Keyboard(self, keyboard: ReplyKeyboardMarkup | InlineKeyboardMarkup | None) -> None:
        ...

    @UserId.setter
    def UserId(self, user_id: str) -> None:
        ...

    async def __call__(self, message: telebot.types.Message, state: StateContext, bot: AsyncTeleBot):
        ...

    async def Endpoint(self) -> None:
        ...