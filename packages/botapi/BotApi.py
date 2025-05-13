from contextlib import _AsyncGeneratorContextManager
from sqlalchemy import over
from telebot.async_telebot import AsyncTeleBot # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Awaitable, Callable, Iterable, overload

from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod

from packages.botmaster import BotMaster
from packages.intefraces import IBotApi, IBotRoute
from packages.intefraces.IBotMaster import IBotMaster

class BotApi:
    
    __bot: AsyncTeleBot
    __botMaster: IBotMaster
    __session: _AsyncGeneratorContextManager
    __handlers: list[IBotRoute.IBotApiRoute]
        
    @AutoProperty[AsyncTeleBot](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    def Bot(self): ...
    
    @AutoProperty[IBotMaster](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    def BotMaster(self): ...
    
    @AutoProperty[_AsyncGeneratorContextManager](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    def Session(self): ...
    
    @overload
    def __iadd__(self, handler: IBotRoute.IBotApiRoute) -> "BotApi": ...
        
    @overload
    def __iadd__(self, handler: Iterable[IBotRoute.IBotApiRoute]) -> "BotApi": ...
    
    def __iadd__(self, handler):
        if isinstance(handler, Iterable[IBotRoute.IBotApiRoute]):
            for i in handler:
                self.AddHandler(i)
        elif isinstance(handler, IBotRoute.IBotApiRoute):
            self.AddHandler(handler)
        else:
            raise TypeError()
    
    def Poll(self) -> None:
        ...
        
    def AddHandler(self, handler: IBotRoute.IBotApiRoute) -> None:
        self.Bot.register_message_handler(
            handler, 
            handler.ContentTypes,
            handler.Commands,
            handler.Regexp,
            handler.Func,
            pass_bot=True
        )
        
    def __init__(self, bot: AsyncTeleBot, botmas: IBotMaster | None, session_maker: _AsyncGeneratorContextManager):
        self.Bot = bot
        self.BotMaster = botmas if botmas is not None else BotMaster(bot)
        self.Session = session_maker