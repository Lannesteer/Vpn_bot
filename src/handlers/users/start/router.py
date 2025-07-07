from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from handlers.users.start.keyboards.commands import main_kb
from handlers.users.start.text import StartTexts

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    user_name = message.from_user.first_name
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
