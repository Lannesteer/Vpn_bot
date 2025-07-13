from aiogram import Router, filters, types, F
from aiogram.fsm.context import FSMContext

from src.filters.admin_filters import AdminFilter
from .keyboards.command import admin_kb
from .text import AdminTexts, AdminButtons
from ...users.start.keyboards.commands import main_kb
from ...users.start.text import StartTexts

router = Router()


@router.message(filters.StateFilter("*"), filters.Command("admin_panel"), AdminFilter())
async def admin_panel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(AdminTexts.StartText, reply_markup=admin_kb())


@router.message(filters.StateFilter("*"), F.text == AdminButtons.Exit, AdminFilter())
async def admin_panel_exit(message: types.Message, state: FSMContext):
    await state.clear()
    user_name = message.from_user.first_name
    await message.answer(
        text=StartTexts.StartText.format(UserName=user_name),
        reply_markup=main_kb()
    )
