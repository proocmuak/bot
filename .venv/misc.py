from aiogram import Bot, Dispatcher
import config
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())