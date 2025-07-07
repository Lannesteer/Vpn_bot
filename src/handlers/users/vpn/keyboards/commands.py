from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType, BotCommand
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from typing import Tuple

del_kb = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(KeyboardButton(text="Ключи 🔑"),
              KeyboardButton(text="Баланс 💰"),
              KeyboardButton(text="Поддержка 👨‍💻"),
              KeyboardButton(text="О нас"))
start_kb2.adjust(2, 2)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="Пополнить баланс 💸"))

cancel_btn = ReplyKeyboardBuilder()
cancel_btn.attach(start_kb2)
cancel_btn.row(KeyboardButton(text="Отменить"))

def get_keyboard(
        *btns: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        sizes: tuple[int, ...] = (2,),
):

    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns, start=0):
        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))
        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placeholder=placeholder
    )
