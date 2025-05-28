from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod
from typing import Any, Callable, Optional
from telebot.states.asyncio.context import StateContext
from telebot.async_telebot import AsyncTeleBot
from telebot.types import (Message,
                           ReplyKeyboardMarkup,
                           InlineKeyboardMarkup,
                           CallbackQuery)


from packages.botapi.state_controller import StateController
from packages.botmaster import BotMaster
from packages.database import get_session
from packages.intefraces.IBotMaster import IBotMaster
from packages.intefraces.IStateController import IStateController


class CallbackApiRoute():

    __callback: CallbackQuery
    __userMessage: Message
    __botmas: IBotMaster
    __stateControl: IStateController
    __userId: str
    
    
    __func: Optional[Callable]
    __keyboard: ReplyKeyboardMarkup
    __inlineKeyboard: InlineKeyboardMarkup

    @AutoProperty[CallbackQuery](annotationType=CallbackQuery,access_mod="public", s_access_mod="protected")
    def Callback(self): ...

    @AutoProperty[Message](annotationType=Message,access_mod="public", s_access_mod="protected")
    def UserMessage(self): ...

    @AutoProperty[BotMaster](annotationType=BotMaster,access_mod="public", s_access_mod="protected")
    def Botmas(self): ...

    @AutoProperty[Callable](annotationType=object,access_mod="public", s_access_mod="protected")
    def Func(self): ...

    @AutoProperty[ReplyKeyboardMarkup | InlineKeyboardMarkup | None](annotationType=ReplyKeyboardMarkup | InlineKeyboardMarkup | None, access_mod="public", s_access_mod="protected")
    def Keyboard(self) -> ReplyKeyboardMarkup | InlineKeyboardMarkup | None: ...

    @AutoProperty[StateController](annotationType=StateController,access_mod=AutoPropAccessMod.Protected)
    def StateControl(self): ...

    @AutoProperty[int](annotationType=int, access_mod="public", s_access_mod="protected")
    def UserId(self): ...
    
    @property
    def Session(self): 
        return get_session()

    def __init__(self):
        """This method is called to initialize the callback for the API .
        """

        ...
        
    async def __call__(self, callback: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> Any:
        self.Callback = callback
        self.StateControl = StateController(state)
        self.Botmas = BotMaster(bot)
        self.UserMessage = self.Callback.message
        self.UserId = self.UserMessage.chat.id