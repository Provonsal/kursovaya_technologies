from typing import Iterable
import autoproperty
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

from packages.intefraces.IKeyboards import IInlineKeyboard, IReplyKeyboard

from autoproperty import AutoProperty

class ReplyKeyboard:
    
    _keyboard: ReplyKeyboardMarkup
    _buttonsCollection: list[KeyboardButton | list[KeyboardButton]]

    def __init__(
        self,
        resizeKeyboard: bool | None = None,
        oneTimeKeyboard: bool | None = None,
        selective: bool | None = None,
        rowWidth: int = 0,
        inputFieldPlaceholder: str | None = None,
        isPersistent: bool | None = None
    ) -> None:

        self._buttonsCollection = list()

        self.Keyboard = ReplyKeyboardMarkup(
            resizeKeyboard,
            oneTimeKeyboard,
            selective,
            rowWidth,
            inputFieldPlaceholder,
            isPersistent
        )
        
        return

    @AutoProperty[ReplyKeyboardMarkup](annotationType=ReplyKeyboardMarkup, access_mod="public", s_access_mod="private")
    def Keyboard(self): ...

    @AutoProperty[list[KeyboardButton | list[KeyboardButton]]](annotationType=list[KeyboardButton | list[KeyboardButton]], access_mod="public", s_access_mod="private")
    def ButtonsCollection(self): ...

    # operator +=
    def __iadd__(self, buttons: list[KeyboardButton] | KeyboardButton) -> "ReplyKeyboard":
        if isinstance(buttons, KeyboardButton):
            self.Keyboard.add(buttons)
            self.ButtonsCollection.append(buttons)
        elif isinstance(buttons, list):
            self.AddButtons(buttons)
        return self

    # operator *=
    def __imul__(self, buttons: list[KeyboardButton] | KeyboardButton) -> "ReplyKeyboard":
        if isinstance(buttons, KeyboardButton):
            self.Keyboard.row(buttons)
            self._buttonsCollection.append([buttons])
        elif isinstance(buttons, list):
            self.AddButtons(buttons)
        else:
            raise TypeError()
        return self

    # public
    def AddButtons(self, buttons: list[KeyboardButton]) -> None:
        self.Keyboard.add(*buttons)
        self.ButtonsCollection.append(buttons)

    def AddRow(self, buttons: list[KeyboardButton]) -> None:
        self.Keyboard.row(*buttons)
        self.ButtonsCollection.append(buttons)
    
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