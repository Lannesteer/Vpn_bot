from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.users.start.text import StartButtons


def cancel_button():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=StartButtons.CancelButton,
        callback_data="cancel"
    )
    builder.adjust()
    return builder.as_markup()