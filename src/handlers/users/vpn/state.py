from aiogram.fsm.state import StatesGroup, State


class VpvState(StatesGroup):
    ChooseCountry = State()
    ChooseServer = State()
