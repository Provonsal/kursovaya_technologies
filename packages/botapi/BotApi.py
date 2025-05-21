import asyncio
from contextlib import _AsyncGeneratorContextManager
from sqlalchemy import over
from telebot.async_telebot import AsyncTeleBot # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Awaitable, Callable, Iterable, overload
from typing_extensions import Self

from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod

from packages.botmaster import BotMaster
from packages.intefraces import IBotApi, IBotRoute
from packages.intefraces.IBotMaster import IBotMaster

class BotApi:
    
    __botMaster: IBotMaster
    __session: _AsyncGeneratorContextManager
    __handlers: list[IBotRoute.IBotApiRoute]
    
    @AutoProperty[IBotMaster](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    def BotMaster(self): ...
    
    @AutoProperty[_AsyncGeneratorContextManager](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    def Session(self): ...
    
    @overload
    def __iadd__(self, handler: IBotRoute.IBotApiRoute) -> Self: ...
        
    @overload
    def __iadd__(self, handler: Iterable[IBotRoute.IBotApiRoute]) -> Self: ...
    
    def __iadd__(self, handler):
        
        if isinstance(handler, Iterable):
            
            for i in handler:
                if isinstance(i, IBotRoute.IBotApiRoute):
                    self.AddHandler(i)
                    self.__handlers.append(i)
                else:
                    raise TypeError()
        elif isinstance(handler, IBotRoute.IBotApiRoute):
            self.AddHandler(handler)
            self.__handlers.append(handler)
        else:
            raise TypeError()
        return self
    
    def Poll(self) -> None:
        asyncio.run(self.BotMaster.Poll())
        
    def AddHandler(self, handler: IBotRoute.IBotApiRoute) -> None:
        self.BotMaster.Bot.register_message_handler(
            handler, # type: ignore
            handler.ContentTypes,
            handler.Commands,
            handler.Regexp,
            handler.Func,
            pass_bot=True
        )
        
    def __init__(self, bot: AsyncTeleBot, botmas: IBotMaster | None, session_maker: _AsyncGeneratorContextManager) -> None:
        self.BotMaster = botmas if botmas is not None else BotMaster(bot)
        self.Session = session_maker