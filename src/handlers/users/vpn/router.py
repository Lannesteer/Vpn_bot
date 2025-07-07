from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from filters.chat_types import ChatTypeFilter
from .keyboards import commands
from .keyboards.callback import get_callback_btns, country_btns
from .state import GetKey

router = Router()

router.message.filter(ChatTypeFilter(['private']))


@router.message(StateFilter("*"), Command("отмена"))
@router.message(StateFilter("*"), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Действия отменены",
                         reply_markup=commands.start_kb2.as_markup(resize_keyboard=True)
                         )


@router.callback_query(F.data.startswith("close_menu"))
async def clouse_menu(callback_query: types.CallbackQuery):
    await callback_query.message.delete()


@router.message(StateFilter('*'), F.text.lower().contains("ключ"))
@router.message(Command('vpn'))
async def get_key(message: types.Message,
                  state: FSMContext,
                  user_id: int,
                  ):
    user_keys = await service.get_user_keys(user_id)

    await message.answer(f"Ваши ключи:",
                         reply_markup=get_callback_btns(btns=user_keys)
                         )

    await state.set_state(GetKey.country)


@router.callback_query(F.data.startswith("get_keys"))
async def select_country(callback_query: types.CallbackQuery,
                         state
                         ):
    await callback_query.message.edit_text("Выберите страну:"),
    await callback_query.message.edit_reply_markup(
        reply_markup=get_callback_btns(btns=country_btns)
    )
    await state.set_state(GetKey.server)


@router.callback_query(F.data.startswith("country_"))
async def server_lst(callback_query: types.CallbackQuery,
                     state: FSMContext,
                     ):
    servers_btns = await service.get_servers_list(callback_query.data)
    await callback_query.message.edit_text("Выберите сервер:")

    await callback_query.message.edit_reply_markup(
        reply_markup=get_callback_btns(btns=servers_btns)
    )
    await state.set_state(GetKey.server_info)


@router.callback_query(F.data.startswith("server_info_"))
async def server_info(callback_query: types.CallbackQuery,
                      state: FSMContext,):
    get_info = await service.get_server_info(callback_query.data)

    await callback_query.message.edit_text(get_info[0], parse_mode="HTML")
    await callback_query.message.edit_reply_markup(
        reply_markup=get_callback_btns(btns=get_info[1])
    )
    await state.set_state(GetKey.key)


@router.callback_query(F.data.startswith("get_key_"))
async def you_key(callback_query: types.CallbackQuery,
                  state: FSMContext,
                  user):
    access_url, text = await service.get_vpn_key(user.telegram_id, callback_query)

    await callback_query.message.edit_text(text, parse_mode="HTML")
    await callback_query.message.answer(f'`{access_url}`', parse_mode='MarkdownV2')

    await state.clear()

# @router.message(F.video)
# async def get_video_id(message: types.Message):
#     video_id = message.video.file_id
#     await message.answer(f"Вот file_id видео: `{video_id}`")
#
#
# @router.message(StateFilter('*'), F.text.lower().contains("тест"))
# async def test(message: types.Message, state: FSMContext):
#     await message.bot.send_video(
#         chat_id=message.chat.id,
#         video='BAACAgIAAxkBAAIL9WfLYBH2Uq7sbR4xW6kqPBf0YdgtAAIXaAACa_5YSvMUFscvj3HdNgQ',
#         caption="Вот инструкция по использованию бота"
#     )

# await message.answer("test",
#                      reply_markup=get_callback_btns(btns={"Сгенерировать ответ 🧠": 'g',
#                                                           "Сгенерировать с учётом пожеланий 💡": 'j',
#                                                           '✅ Позитивные': "positive",
#                                                           '😐 Нейтральные': "neytral",
#                                                           '❌ Негативные': 'negative',
#                                                           'Вернуться 🔙': 'back',
#                                                            "На главную 🏠": 'home'},
#                                                     sizes=(1, 1, 1, 1, 1, 2)
#                                                     ))
