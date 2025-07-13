from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.handlers.admins.admin_panel.text import AdminButtons


def admin_kb():
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton(text=AdminButtons.ServersControl),
                KeyboardButton(text=AdminButtons.Statistic),
                KeyboardButton(text=AdminButtons.Exit)
                )

    builder.adjust(1, 1)

    return builder.as_markup(resize_keyboard=True)