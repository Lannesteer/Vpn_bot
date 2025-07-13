from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.database.users.service import user_service
from .keyboards.commands import main_kb
from .text import StartTexts

router = Router()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    user_name = message.from_user.first_name
    await user_service.check_user_and_add(message.from_user.id)
    await message.answer(
        text=StartTexts.StartText.format(UserName=user_name),
        reply_markup=main_kb()
    )


@router.message(F.text.lower().contains('баланс'))
@router.message(Command('balance'))
async def balance(message: types.Message):
    pass


@router.message(F.text.lower().contains("поддержка"))
@router.message(Command('support'))
async def support(message: types.Message):
    pass


@router.message(F.text.lower().contains("о нас"))
@router.message(Command('about'))
async def about(message: types.Message):
    pass


@router.callback_query(F.data == "cancel")
async def cancel(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.delete()
