from aiogram.types import BotCommand, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from handlers.users.start.text import StartButton

commands = [
    BotCommand(command="start", description="Start"),
]


def main_kb():
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton(text=StartButton.KeysButton),
                KeyboardButton(text=StartButton.BalanceButton),
                KeyboardButton(text=StartButton.SupportButton),
                KeyboardButton(text=StartButton.AboutButton))

    builder.adjust(2, 2)

    return builder.as_markup(resize_keyboard=True)
