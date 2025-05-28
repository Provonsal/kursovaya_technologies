import os

from config import Config
from packages.botapi.base_callback_route import CallbackApiRoute
os.environ['PYTHONASYNCIODEBUG'] = '1'
import asyncio
from contextlib import _AsyncGeneratorContextManager
from sqlalchemy import over
from telebot.async_telebot import AsyncTeleBot # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Awaitable, Callable, Iterable, overload
from typing_extensions import Self

from autoproperty import AutoProperty
from autoproperty.prop_settings import AutoPropAccessMod

from packages.botapi.base_route import BaseBotRoute
from packages.botmaster import BotMaster
from packages.database import init_db
from packages.intefraces import IBotApi, IBotRoute
from packages.intefraces.IBotMaster import IBotMaster

class BotApi:
    
    _botMaster: IBotMaster
    __session: _AsyncGeneratorContextManager[AsyncSession]
    __handlers: list
    
    @AutoProperty[IBotMaster](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    def BotMaster(self, v: IBotMaster): ...
    
    # @AutoProperty[_AsyncGeneratorContextManager[AsyncSession]](access_mod=AutoPropAccessMod.Public, s_access_mod=AutoPropAccessMod.Protected)
    # def Session(self): ...
    
    @overload
    def __iadd__(self, handler: BaseBotRoute) -> Self: ...
        
    @overload
    def __iadd__(self, handler: Iterable[BaseBotRoute]) -> Self: ...
    
    def __iadd__(self, handler):
        
        if isinstance(handler, Iterable):
            
            for i in handler:
                if isinstance(i, BaseBotRoute):
                    self.AddHandler(i)
                    self.__handlers.append(i)
                else:
                    raise TypeError()
        elif isinstance(handler, BaseBotRoute):
            self.AddHandler(handler)
            self.__handlers.append(handler)
        else:
            raise TypeError()
        return self
    
    @overload
    def __imul__(self, handler: CallbackApiRoute) -> Self: ...
        
    @overload
    def __imul__(self, handler: Iterable[CallbackApiRoute]) -> Self: ...
    
    def __imul__(self, handler):
        
        if isinstance(handler, Iterable):
            
            for i in handler:
                if isinstance(i, CallbackApiRoute):
                    self.AddCallBackHandler(i)
                    self.__handlers.append(i)
                else:
                    raise TypeError()
        elif isinstance(handler, CallbackApiRoute):
            self.AddCallBackHandler(handler)
            self.__handlers.append(handler)
        else:
            raise TypeError()
        return self
    
    def Poll(self) -> None:
        asyncio.run(self.BotMaster.Poll(), debug=bool(int(Config.GetValue("ASYNC_DEBUG"))))
        
    def AddHandler(self, handler: BaseBotRoute) -> None:
        self.BotMaster.Bot.register_message_handler(
            handler, # type: ignore
            handler.ContentTypes,
            handler.Commands,
            handler.Regexp,
            handler.Func,
            is_digit=handler.IsDigit,
            pass_bot=True
        )
        
    def AddCallBackHandler(self, handler: CallbackApiRoute):
        self.BotMaster.Bot.register_callback_query_handler(
            handler, # type: ignore
            handler.Func,
            pass_bot=True
        )
        
    def __init__(self, bot: AsyncTeleBot, botmas: IBotMaster | None = None) -> None:
        self.BotMaster = botmas if botmas is not None else BotMaster(bot)
        self.__handlers = []