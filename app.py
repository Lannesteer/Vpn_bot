import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllPrivateChats

from database import get_async_session
from src.bot.middlewares.db import UserIDMiddleware, DataBaseSession
from src.bot.cmd_list import private
from src.config import bot_token

from src.bot.handlers.keys.router import router as keys_router

# ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(
    token=bot_token.access_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)


async def app():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    dp = Dispatcher()

    dp.include_router(keys_router)
    dp.update.middleware(UserIDMiddleware())
    dp.update.middleware(DataBaseSession(get_async_session()))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(app())
