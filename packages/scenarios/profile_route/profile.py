from typing import cast
from uuid import uuid4
from telebot.async_telebot import AsyncTeleBot
from telebot.states.asyncio.context import StateContext
from telebot.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup
from packages.botapi.base_callback_route import CallbackApiRoute
from packages.keyboard import InlineKeyboard
from packages.database.schemas.user import User
from packages.database.schemas.role import Role


class CB_Profile(CallbackApiRoute):
    def __init__(self) -> None:
        super().__init__()
        
        self.Func = lambda callback: callback.data == "ProfileRouteStart"
        
        inl_kb = InlineKeyboard()
        
        inl_kb += InlineKeyboardButton("Назад", callback_data="mainmenu")
        
        self.Keyboard = inl_kb.Keyboard
        
    async def __call__(self, message: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> None:
        await super().__call__(message, state, bot)
        
        user = await User.get_by_telegramId(self.Session, self.UserId)
        
        if user:
            role = await Role.get(self.Session, user.RoleId)
            name_line = f"Name: {self.UserMessage.chat.first_name}"
            lastname_line = f"Lastname: {self.UserMessage.chat.last_name}"
            id_line = f"Id: {user.TelegramId}"
            subscription_line= f"Has subscription: {user.IsVip}"
            role_line = f"Role: {role.RoleName}" if role is not None else "Role: unknown"
            phone_line = f"Phone: {user.PhoneNumber}" if user.PhoneNumber is not None else "Phone: unknown"
            
            self.bot_message = "\n".join((name_line, lastname_line, id_line, subscription_line, role_line, phone_line))
            
            await self.Botmas.EditMessage(self.bot_message, self.UserId, self.UserMessage.message_id, cast(InlineKeyboardMarkup, self.Keyboard))
        else:
            await self.Botmas.EditMessage("Извините, информация о вас не найдена. Пожалуйста обратитесь к администратору:\n@Provonsal", self.UserId, self.UserMessage.message_id, cast(InlineKeyboardMarkup, self.Keyboard))
            
        
        