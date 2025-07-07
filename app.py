import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllPrivateChats

from src.middlewares.db import SessionMiddleware
from src.middlewares.user import UserMiddleware
from src.handlers.users.start.keyboards.commands import commands
from src.config import BotToken

from handlers.users.vpn.router import router as vpn_router
from handlers.users.start.router import router as start_router


async def app():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    bot = Bot(
        token=BotToken.access_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    dp.update.middleware(SessionMiddleware())
    dp.message.outer_middleware(UserMiddleware)
    dp.callback_query.outer_middleware(UserMiddleware)

    dp.include_router(vpn_router)
    dp.include_router(start_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(app())
