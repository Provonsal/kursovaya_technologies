from typing import Any, cast
from uuid import uuid4
from telebot.async_telebot import AsyncTeleBot
from telebot.states.asyncio.context import StateContext, StatesGroup, State
from telebot.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, KeyboardButton, Message
from packages.botapi.base_callback_route import CallbackApiRoute
from packages.botapi.base_route import BaseBotRoute
from packages.keyboard import InlineKeyboard, ReplyKeyboard
from packages.database.schemas.user import User
from packages.database.schemas.role import Role
from packages.database.schemas.offer import Offer
import os


class CreateOfferGroup(StatesGroup):
    GetLabel = State()
    GetPhoto = State()

class CB_OfferOptions(CallbackApiRoute):
    def __init__(self) -> None:
        super().__init__()
        
        self.Func = lambda callback: callback.data == "ProfileRouteStart"
        
        inl_kb = InlineKeyboard()
        
        inl_kb += InlineKeyboardButton("Изменить объявление", callback_data="change_offer")
        inl_kb += InlineKeyboardButton("Создать новое объявление", callback_data="create_new_one_offer")
        inl_kb += InlineKeyboardButton("Удалить объявление", callback_data="delete_offer")
        
        self.Keyboard = inl_kb.Keyboard

        self.bot_message = "Что вы хотите сделать?"
        
    async def __call__(self, message: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> None:
        await super().__call__(message, state, bot)
        
        user = await User.get_by_telegramId(self.Session, self.UserId)
        
        await self.Botmas.edit_message(self.bot_message, self.UserId, self.UserMessage.message_id, cast(InlineKeyboardMarkup, self.Keyboard))
        
class CB_OfferCreate(CallbackApiRoute):
    def __init__(self) -> None:
        super().__init__()
        
        self.Func = lambda callback: callback.data == "create_new_one_offer"
        
        self.bot_message = "Write text of your offer, for example:\nSell \nroyal hat t4.0 за 20к\nmercinary kurtka t6.3 за 500к"
    
    async def __call__(self, callback: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> Any:
        await super().__call__(callback, state, bot)
        
        await self.StateControl.SetNextState(CreateOfferGroup.GetLabel)
        
        await self.Botmas.edit_message(self.bot_message, self.UserId, self.UserMessage.message_id)
        
class API_OfferCreate_GotLabel(CallbackApiRoute):
    def __init__(self):
        super().__init__()
        
        self.StateControl = CreateOfferGroup.GetLabel
        
        self.bot_message = f"Send a photo for your offer, or press button 'No photo'"
        
        rp_kb = ReplyKeyboard()
        
        rp_kb += KeyboardButton("No photo")
        
        self.Keyboard = rp_kb.Keyboard
        
        
    async def __call__(self, callback: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> Any:
        await super().__call__(callback, state, bot)
        
        await self.StateControl.SetNextState(CreateOfferGroup.GetPhoto)
        
        await self.StateControl.AddDataState(Label=self.UserMessage.text)
        
        
class API_OfferCreate_GotPhoto(BaseBotRoute):
    def __init__(self):
        super().__init__()
        
        #self.StateControl = CreateOfferGroup.GetLabel
        
        self.ContentTypes = ['photo']
        
        self.bot_message = f"Choose tags"
        
        rp_kb = ReplyKeyboard()
        
        rp_kb += KeyboardButton("Placeholder tags")
        
        self.Keyboard = rp_kb.Keyboard
        
    async def __call__(self, message: Message, state: StateContext, bot: AsyncTeleBot) -> Any:
        await super().__call__(message, state, bot)
        
        await self.StateControl.SetNextState(CreateOfferGroup.GetPhoto)
        
        await self.StateControl.AddDataState(PhotoPath=self.UsersMessage.text)
        
        self.image_path = f"users_offers/{self.UserId}/offer/offer_image.jpg"
        
        self.image_path = os.path.join(os.getcwd(), self.image_path)
        
        await self.StateControl.AddDataState(GotPhoto=self.image_path)

        if self.UsersMessage.photo is not None:
            self.file_id = self.UsersMessage.photo[-1].file_id

        # скачивание и запись фото
        file_info = await bot.get_file(self.file_id)

        downloaded_file = await bot.download_file(file_info.file_path)

        with open(self.image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        
        
class CB_OfferShow(CallbackApiRoute):
    def __init__(self) -> None:
        super().__init__()
        
        self.Func = lambda callback: callback.data == "ShowOwnOfferRouteStart"
        
        inl_kb = InlineKeyboard()
        
        inl_kb += InlineKeyboardButton("Назад", callback_data="mainmenu")
        
        self.not_found_offer_text = "Объявление не найдено. Хотите создать?"
        
        self.keyboard_when_notfound = InlineKeyboard()
        
        self.keyboard_when_notfound += InlineKeyboardButton("Создать объявление", callback_data="create_new_one_offer")
        self.keyboard_when_notfound += InlineKeyboardButton("Назад", callback_data="mainmenu")
        
        self.Keyboard = inl_kb.Keyboard
        
    async def __call__(self, message: CallbackQuery, state: StateContext, bot: AsyncTeleBot) -> None:
        await super().__call__(message, state, bot)
        
        user = await User.get_by_telegramId(self.Session, self.UserId)
        if user is not None:
            own_offer = await Offer.get(self.Session, user.UserId)
            if own_offer is not None:
                tags_list_str = "\n".join(own_offer.Tags)
                qualities_list_str = "\n".join(own_offer.Tiers)
                tiers_list_str = "\n".join(own_offer.Tiers)
                self.bot_message = f"{own_offer.Label}\n\nTags:\n{tags_list_str}\nQualities:\n{qualities_list_str}\nTiers:\n{tiers_list_str}"
                
                if own_offer.PhotoPath is not None:
                    with open(own_offer.PhotoPath, "rb") as photo:
                        await self.Botmas.send_photo(photo=photo,caption=self.bot_message, user_id=self.UserId, reply_markup=cast(InlineKeyboardMarkup, self.Keyboard))
                else:
                    await self.Botmas.edit_message(self.bot_message, self.UserId, self.UserMessage.message_id, reply_markup=cast(InlineKeyboardMarkup, self.Keyboard))
            else:
                await self.Botmas.edit_message(self.not_found_offer_text, self.UserId, self.UserMessage.message_id, reply_markup=self.keyboard_when_notfound.Keyboard)