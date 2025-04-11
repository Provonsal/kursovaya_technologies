from typing import Iterable
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

from packages.intefraces.IKeyboards import IInlineKeyboard, IReplyKeyboard

class ReplyKeyboard:
    
    _keyboard: ReplyKeyboardMarkup
    _buttonsCollection: Iterable[KeyboardButton]
    
    @property
    def Keyboard(self) -> ReplyKeyboardMarkup:
        return self._keyboard
        
    @Keyboard.setter
    def Keyboard(self, keyboard: ReplyKeyboardMarkup):
        if isinstance(keyboard, ReplyKeyboardMarkup):
            self._keyboard = keyboard
        else:
            raise Exception()
    
    # operator +=
    def __iadd__(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> "IReplyKeyboard":
        self.AddButtons(buttons)
        return self

    # operator *=
    def __imul__(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> "IReplyKeyboard":
        self.AddRow(buttons)
        return self

    # public 
    def AddButtons(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> None:
        if isinstance(buttons, Iterable):
            self._keyboard.add(*buttons)
        elif isinstance(buttons, KeyboardButton):
            self._keyboard.add(buttons)
        else:
            raise Exception()
    
    def AddRow(self, buttons: Iterable[KeyboardButton] | KeyboardButton) -> None:
        if isinstance(buttons, Iterable):
            self._keyboard.row(*buttons)
        elif isinstance(buttons, KeyboardButton):
            self._keyboard.row(buttons)
        else:
            raise Exception()
    
class InlineKeyboard:
    
    _keyboard: InlineKeyboardMarkup
    _buttonsCollection: Iterable[InlineKeyboardButton]
    
    @property
    def Keyboard(self) -> InlineKeyboardMarkup:
        return self._keyboard
        
    @Keyboard.setter
    def Keyboard(self, keyboard: InlineKeyboardMarkup):
        if isinstance(keyboard, InlineKeyboardMarkup):
            self._keyboard = keyboard
        else:
            raise Exception()
    
    # operator +=
    def __iadd__(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> "IInlineKeyboard":
        self.AddButtons(buttons)
        return self

    # operator *=
    def __imul__(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> "IInlineKeyboard":
        self.AddRow(buttons)
        return self

    # public 
    def AddButtons(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> None:
        if isinstance(buttons, Iterable):
            self._keyboard.add(*buttons)
        elif isinstance(buttons, KeyboardButton):
            self._keyboard.add(buttons)
        else:
            raise Exception()
    
    def AddRow(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> None:
        if isinstance(buttons, Iterable):
            self._keyboard.row(*buttons)
        elif isinstance(buttons, KeyboardButton):
            self._keyboard.row(buttons)
        else:
            raise Exception()