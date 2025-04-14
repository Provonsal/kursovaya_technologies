from typing import Iterable
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from tomlkit import key

from packages.validator import FieldValidator


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

    @property
    def Keyboard(self) -> ReplyKeyboardMarkup:
        return self._keyboard

    @Keyboard.setter
    @FieldValidator("_keyboard", ReplyKeyboardMarkup)
    def Keyboard(self, keyboard: ReplyKeyboardMarkup) -> None:
        self._keyboard = keyboard

    @property
    def ButtonsCollection(self) -> list[KeyboardButton | list[KeyboardButton]]:
        return self._buttonsCollection

    @ButtonsCollection.setter
    @FieldValidator("_buttonsCollection", Iterable[KeyboardButton | Iterable[KeyboardButton]])
    def ButtonsCollection(self, buttonCollection: list[KeyboardButton | list[KeyboardButton]]) -> None:
        self._buttonsCollection = buttonCollection

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
    _buttonsCollection: list[InlineKeyboardButton | list[InlineKeyboardButton]]

    def __init__(self, rowWidth: int) -> None:
        self.Keyboard = InlineKeyboardMarkup(row_width=rowWidth)

    @property
    def Keyboard(self) -> InlineKeyboardMarkup:
        return self._keyboard

    @Keyboard.setter
    @FieldValidator("_keyboard", InlineKeyboardMarkup)
    def Keyboard(self, keyboard: InlineKeyboardMarkup):
        self._keyboard = keyboard

    @property
    def ButtonsCollection(self) -> list[InlineKeyboardButton | list[InlineKeyboardButton]]:
        return self._buttonsCollection
    
    @ButtonsCollection.setter
    @FieldValidator("_buttonsCollection", Iterable[KeyboardButton | Iterable[KeyboardButton]])
    def ButtonsCollection(self, buttonsCollection: list[InlineKeyboardButton | list[InlineKeyboardButton]]) -> None:
        self._buttonsCollection = buttonsCollection

    # operator +=
    def __iadd__(self, buttons: list[InlineKeyboardButton] | InlineKeyboardButton) -> "InlineKeyboard":
        if isinstance(buttons, InlineKeyboardButton):
            self.Keyboard.add(buttons)
            self.ButtonsCollection.append(buttons)
        elif isinstance(buttons, Iterable):
            self.AddButtons(buttons)
        return self

    # operator *=
    def __imul__(self, buttons: list[InlineKeyboardButton] | InlineKeyboardButton) -> "InlineKeyboard":
        if isinstance(buttons, InlineKeyboardButton):
            self.Keyboard.row(buttons)
            self.ButtonsCollection.append(buttons)
        elif isinstance(buttons, Iterable):
            self.AddButtons(buttons)
        return self

    # public
    def AddButtons(self, buttons: list[InlineKeyboardButton]) -> None:
        self.Keyboard.add(*buttons)
        self.ButtonsCollection.append(buttons)

    def AddRow(self, buttons: list[InlineKeyboardButton]) -> None:
        self.Keyboard.row(*buttons)
        self.ButtonsCollection.append(buttons)
