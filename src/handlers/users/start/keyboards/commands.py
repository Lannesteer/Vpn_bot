from aiogram.types import BotCommand, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.handlers.users.start.text import StartButtons

commands = [
    BotCommand(command="start", description="Start"),
]


def main_kb():
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton(text=StartButtons.KeysButton),
                KeyboardButton(text=StartButtons.BalanceButton),
                KeyboardButton(text=StartButtons.SupportButton),
                KeyboardButton(text=StartButtons.AboutButton))

    builder.adjust(2, 2)

    return builder.as_markup(resize_keyboard=True)
