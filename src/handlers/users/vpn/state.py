from aiogram.fsm.state import StatesGroup, State


class GetKey(StatesGroup):
    country = State()
    server = State()
    server_info = State()
    key = State()
