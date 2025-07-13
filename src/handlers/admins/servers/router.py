from aiogram import Router, filters, F, types
from aiogram.fsm.context import FSMContext

from src.database.servers.state import ServerState
from src.filters.admin_filters import AdminFilter
from src.handlers.admins.admin_panel.text import AdminButtons
from .keyboard.callback import ServersCallBacks, ServersKeyboardsCallBacks
from .text import ServerTexts
from src.handlers.admins.service import admin_service

router = Router()


@router.message(filters.StateFilter("*"), F.text == AdminButtons.ServersControl, AdminFilter())
async def servers_control_panel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=ServerTexts.SelectActionText,
        reply_markup=ServersKeyboardsCallBacks.ServersControl(
            add=True
        )
    )


@router.callback_query(ServersCallBacks.ServersCB.filter(), filters.StateFilter("*"))
async def add_server(call: types.CallbackQuery,
                     callback_data: ServersCallBacks.ServersCB,
                     state: FSMContext):
    if callback_data.action == "add_server":
        await call.message.edit_text(text=ServerTexts.EnterType)
        await state.set_state(ServerState.Type)
    elif callback_data.action == "confirm":
        data = await state.get_data()
        await admin_service.add_server(data)
        await call.message.edit_text(ServerTexts.ServerAdded)
        await state.clear()


@router.message(filters.StateFilter(ServerState.Type))
async def enter_server_type(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)
    await message.answer(text=ServerTexts.EnterCountry)
    await state.set_state(ServerState.Country)


@router.message(filters.StateFilter(ServerState.Country))
async def enter_server_country(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await message.answer(text=ServerTexts.EnterPrice)
    await state.set_state(ServerState.Price)


@router.message(filters.StateFilter(ServerState.Price))
async def enter_server_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await message.answer(
        text=ServerTexts.ConfirmAction.format(
            Type=data.get("type"),
            Country=data.get("country"),
            Price=data.get("price")
        ),
        reply_markup=ServersKeyboardsCallBacks.ServersControl(confirm=True)
    )
