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

    @AutoProperty[ReplyKeyboardMarkup](annotationType=ReplyKeyboardMarkup, access_mod="public", s_access_mod="protected")
    def Keyboard(self): ...

    @AutoProperty[list[KeyboardButton | list[KeyboardButton]]](annotationType=list[KeyboardButton | list[KeyboardButton]], access_mod="public", s_access_mod="protected")
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
    
    __keyboard: InlineKeyboardMarkup
    __buttonsCollection: list
    
    def __init__(self, row_width: int = 1) -> None:
        self.Keyboard = InlineKeyboardMarkup(row_width=row_width)
        self.ButtonsCollection = []
    
    @AutoProperty[InlineKeyboardMarkup](access_mod='public')
    def Keyboard(self, v: InlineKeyboardMarkup): ...
    
    @AutoProperty[list[InlineKeyboardButton | list[InlineKeyboardButton]]](access_mod="public", s_access_mod="protected")
    def ButtonsCollection(self, v: list): ...
    
    # operator +=
    def __iadd__(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> "InlineKeyboard":
        self.add_buttons(buttons)
        return self

    # operator *=
    def __imul__(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> "InlineKeyboard":
        self.add_row(buttons)
        return self

    # public 
    def add_buttons(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> None:
        if isinstance(buttons, Iterable):
            self.Keyboard.add(*buttons)
        elif isinstance(buttons, InlineKeyboardButton):
            self.Keyboard.add(buttons)
        else:
            raise TypeError()
    
    def add_row(self, buttons: Iterable[InlineKeyboardButton] | InlineKeyboardButton) -> None:
        if isinstance(buttons, Iterable):
            self.Keyboard.row(*buttons)
        elif isinstance(buttons, InlineKeyboardButton):
            self.Keyboard.row(buttons)
        else:
            raise TypeError()