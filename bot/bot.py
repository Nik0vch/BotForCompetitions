import os, logging
from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=os.environ['BOT_TOKEN'], parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

from .handlers import router #импорт после инициализации бота во избежании ошибки зацикливония
dp.include_router(router)

async def bot_run():
    logging.getLogger("aiogram").setLevel(logging.WARNING)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

async def bot_stop():
    await dp.stop_polling()


