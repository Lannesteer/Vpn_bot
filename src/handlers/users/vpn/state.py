from aiogram.fsm.state import StatesGroup, State


class VpvState(StatesGroup):
    Country = State()
    Server = State()
    ServerInfo = State()
    Key = State()
