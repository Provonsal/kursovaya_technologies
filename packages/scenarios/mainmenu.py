
import os
from typing import cast
from uuid import uuid4
from telebot.async_telebot import AsyncTeleBot
from telebot.states.asyncio.context import StateContext
from telebot.types import InlineKeyboardButton, Message, CallbackQuery, InlineKeyboardMarkup
from packages.botapi.base_route import BaseBotRoute
from packages.botapi.base_callback_route import CallbackApiRoute
from packages.keyboard import InlineKeyboard
from packages.database.schemas.user import User


class API_Mainmenu(BaseBotRoute):
    def __init__(self) -> None:
        super().__init__()
        
        self.Commands = ('start', 'mainmenu')
        
        inl_kb = InlineKeyboard()
        
        inl_kb += InlineKeyboardButton("Профиль", callback_data="ProfileRouteStart")
        inl_kb += InlineKeyboardButton("Увидеть свое объявление", callback_data="ShowOwnOfferRouteStart")
        inl_kb += InlineKeyboardButton("Управление своим объявлением", callback_data="ManageRouteStart")
        inl_kb += InlineKeyboardButton("Искать предложения", callback_data="LookForOffersRouteStart")
        inl_kb += InlineKeyboardButton("Управление подпиской", callback_data="ManageSubscriptionRouteStart")
        
        self.Keyboard = inl_kb.Keyboard
        
        self.bot_message: str = "Главное меню" 
        
    async def __call__(self, message: Message, state: StateContext, bot: AsyncTeleBot) -> None:
        await super().__call__(message, state, bot)
        await self.StateControl.ResetStates()
        await self.Botmas.send_message(self.UserId, self.bot_message, self.Keyboard)
        
        user = User(user_id=uuid4(), telegram_id=self.UserId)
        
        await user.create(self.Session)
        
        user = await User.get_by_telegramId(self.Session, self.UserId)
        if user is not None:
            user_personaly_path = f"./users_offers/{user.UserId}/offer/"
            if not os.path.exists(user_personaly_path):
                os.mkdir(f"./users_offers/{user.UserId}/")
                os.mkdir(user_personaly_path)
    
class CB_MainMenu(CallbackApiRoute):
    def __init__(self) -> None:
        super().__init__()
        
        self.Func = lambda callback: callback.data == "mainmenu"
        
        inl_kb = InlineKeyboard()
        
        inl_kb += InlineKeyboardButton("Профиль", callback_data="ProfileRouteStart")
        inl_kb += InlineKeyboardButton("Увидеть свое объявление", callback_data="ShowOwnOfferRouteStart")
        inl_kb += InlineKeyboardButton("Управление своим объявлением", callback_data="ManageRouteStart")
        inl_kb += InlineKeyboardButton("Искать предложения", callback_data="LookForOffersRouteStart")
        inl_kb += InlineKeyboardButton("Управление подпиской", callback_data="ManageSubscriptionRouteStart")
        
        self.Keyboard = inl_kb.Keyboard
        
        self.bot_message: str = "Главное меню" 
        
    async def __call__(self, message: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> None:
        await super().__call__(message, state, bot)
        self.Callback.data
        await self.StateControl.ResetStates()
        await self.Botmas.edit_message(self.bot_message, self.UserId, self.UserMessage.message_id, cast(InlineKeyboardMarkup, self.Keyboard))
        
        user = User(user_id=uuid4(), telegram_id=self.UserId)
        
        await user.create(self.Session)
        
        user = await User.get_by_telegramId(self.Session, self.UserId)
        
        if user is not None:
            user_personaly_path = f"./users_offers/{user.UserId}/offer/"
            if not os.path.exists(user_personaly_path):
                os.mkdir(f"./users_offers/{user.UserId}/")
                os.mkdir(user_personaly_path)