from typing import Iterable, Protocol
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


class IReplyKeyboard(Protocol):
    
    _keyboard: ReplyKeyboardMarkup
    _buttonsCollection: Iterable[KeyboardButton]
    
    @property
    def Keyboard(self) -> ReplyKeyboardMarkup:
        ...
        
    @Keyboard.setter
    def Keyboard(self, keyboard: ReplyKeyboardMarkup):
        ...
    
    @property
    def ButtonsCollection(self) -> Iterable[KeyboardButton]:
        ...
    
    @ButtonsCollection.setter
    def ButtonsCollection(self, buttonCollection: Iterable[KeyboardButton]) -> None:
        ...
    
    # operator +=
    def __iadd__(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> "IReplyKeyboard":
        ...

    # operator *=
    def __imul__(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> "IReplyKeyboard":
        ...

    # public 
    def AddButtons(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> None:
        ...
    
    def AddRow(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> None:
        ...

class IInlineKeyboard(Protocol):
    
    _keyboard: InlineKeyboardMarkup
    _buttonsCollection: Iterable[InlineKeyboardButton]
    
    @property
    def Keyboard(self) -> InlineKeyboardMarkup:
        ...
        
    @Keyboard.setter
    def Keyboard(self, keyboard: InlineKeyboardMarkup):
        ...
    
    @property
    def ButtonsCollection(self) -> Iterable[KeyboardButton]:
        ...
    
    @ButtonsCollection.setter
    def ButtonsCollection(self, buttonCollection: Iterable[KeyboardButton]) -> None:
        ...
    
    # operator +=
    def __iadd__(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> "IInlineKeyboard":
        ...

    # operator *=
    def __imul__(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> "IInlineKeyboard":
        ...

    # public 
    def AddButtons(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> None:
        ...
    
    def AddRow(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> None:
        ...
        