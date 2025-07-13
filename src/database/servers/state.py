from aiogram.fsm.state import StatesGroup, State


class ServerState(StatesGroup):
    Type = State()
    Country = State()
    Price = State()


