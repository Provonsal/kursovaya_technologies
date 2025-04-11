

from types import NoneType
from typing import Iterable, Optional, Union, Callable

from telebot.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup

from telebot.states import State

from telebot.states.asyncio.context import StateContext # type: ignore

from packages.botmaster import BotMaster
from packages.intefraces.IBotMaster import IBotMaster

from telebot.async_telebot import AsyncTeleBot

import telebot

from packages.intefraces.IStateController import IStateController


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
    def MMessage(self) -> Message | None:
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
    
        
    @MMessage.setter
    def MMessage(self, message: telebot.types.Message | None) -> None:
        if isinstance(message, (telebot.types.Message, NoneType)):
            self._message = message
        else:
            raise TypeError(f"Argument {self._message} is not a {telebot.types.Message} type.")
    
    
    @Botmas.setter
    def Botmas(self, botmas: IBotMaster | None) -> None:
        if isinstance(botmas, (IBotMaster, NoneType)):
            self._botmas = botmas
        else:
            raise TypeError(f"Argument {self._botmas} is not a {IBotMaster} type.")

    
    @Commands.setter
    def Commands(self, commands: Iterable[str]) -> None:
        if isinstance(commands, Iterable):
            self._commands = commands
        else:
            raise TypeError(f"Argument {self._commands} is not a {Iterable} type.")
    
    
    @ContentTypes.setter
    def ContentTypes(self, contenTypes: Iterable[str]) -> None:
        if isinstance(contenTypes, Iterable):
            self._contenTypes = contenTypes
        else:
            raise TypeError(f"Argument {self._contenTypes} is not a {Iterable} type.")
    
    
    @Regexp.setter
    def Regexp(self, regexp: str) -> None:
        if isinstance(regexp, str):
            self._regexp = regexp
        else:
            raise TypeError(f"Argument {self._regexp} is not a {str} type.")
    
    
    @Func.setter
    def Func(self, func: Callable | None) -> None:
        if isinstance(func, (Callable, NoneType)):
            self._func = func
        else:
            raise TypeError(f"Argument {self._func} is not a {Union[Callable, NoneType]} or None type.")
    
    
    @StatmentState.setter
    def StatmentState(self, state: State | str | None) -> None:
        if isinstance(state, (State, str, NoneType)):
            self._state = state
        else:
            raise TypeError(f"Argument {self._state} is not a {Union[State, str, NoneType]} or None type.")
    

    @IsDigit.setter
    def IsDigit(self, isDigit: bool | None) -> None:
        if isinstance(isDigit, (bool, NoneType)):
            self._is_digit = isDigit
        else:
            raise TypeError(f"Argument {self._is_digit} is not a {Union[bool, NoneType]} or None type.")
    

    @Keyboard.setter
    def Keyboard(self, keyboard: ReplyKeyboardMarkup | InlineKeyboardMarkup | None) -> None:
        if isinstance(keyboard, (ReplyKeyboardMarkup, InlineKeyboardMarkup, NoneType)):
            self._keyboard = keyboard
        else:
            raise TypeError(f"Argument {self._keyboard} is not a {Union[bool, NoneType]} or None type.")
        

    @UserId.setter
    def UserId(self, user_id: str) -> None:
        if isinstance(user_id, (str)):
            self._user_id = user_id
        else:
            raise TypeError(f"Argument {self._keyboard} is not a {Union[bool, NoneType]} or None type.")
        
    async def __call__(self, message: telebot.types.Message, state: StateContext, bot: AsyncTeleBot):
        self.Botmas = BotMaster(bot)
        self.MMessage = message
        self.ContextState = state
        if self.MMessage is not None:
            self._user_id: str = str(self.MMessage.chat)
            
    async def Endpoint(self) -> None:
        raise NotImplementedError()
        