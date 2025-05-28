from config import Config
from packages.botapi.bot_api import BotApi
from telebot.async_telebot import AsyncTeleBot

from packages.scenarios.mainmenu import API_Mainmenu, CB_MainMenu
from telebot.asyncio_storage import StateRedisStorage

from packages.scenarios.offer_manage_route.offer_manage import CB_OfferOptions, CB_OfferShow
from packages.scenarios.profile_route.profile import CB_Profile

redis_store = StateRedisStorage()

bot = AsyncTeleBot(Config.GetValue("TOKEN"), state_storage=redis_store)

app = BotApi(bot)

app += API_Mainmenu()
app *= CB_MainMenu()
app *= CB_Profile()
app *= CB_OfferOptions()
app *= CB_OfferShow()

app.Poll()