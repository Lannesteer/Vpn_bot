from aiogram import types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.database.users.service import user_service
from .keyboards.callback import VpnKeyboardsCallBacks
from aiogram import Router

from .text import VpnTexts
from ..start.text import StartButtons

router = Router()


# @router.callback_query(F.data.startswith("close_menu"))
# async def clouse_menu(callback_query: types.CallbackQuery):
#     await callback_query.message.delete()


@router.message(StateFilter('*'), F.text == StartButtons.KeysButton)
async def get_user_keys(message: types.Message,
                        state: FSMContext,
                        user):
    user_keys = await user_service.get_all_user_keys(user.id)
    await message.answer(
        text=VpnTexts.UserKeys,
        reply_markup=VpnKeyboardsCallBacks.Keys(keys=user_keys)
    )

# @router.callback_query(F.data.startswith("get_keys"))
# async def select_country(callback_query: types.CallbackQuery,
#                          state
#                          ):
#     await callback_query.message.edit_text("Выберите страну:"),
#     await callback_query.message.edit_reply_markup(
#         reply_markup=get_callback_btns(btns=country_btns)
#     )
#     await state.set_state(GetKey.server)
#
#
# @router.callback_query(F.data.startswith("country_"))
# async def server_lst(callback_query: types.CallbackQuery,
#                      state: FSMContext,
#                      ):
#     servers_btns = await service.get_servers_list(callback_query.data)
#     await callback_query.message.edit_text("Выберите сервер:")
#
#     await callback_query.message.edit_reply_markup(
#         reply_markup=get_callback_btns(btns=servers_btns)
#     )
#     await state.set_state(GetKey.server_info)
#
#
# @router.callback_query(F.data.startswith("server_info_"))
# async def server_info(callback_query: types.CallbackQuery,
#                       state: FSMContext,):
#     get_info = await service.get_server_info(callback_query.data)
#
#     await callback_query.message.edit_text(get_info[0], parse_mode="HTML")
#     await callback_query.message.edit_reply_markup(
#         reply_markup=get_callback_btns(btns=get_info[1])
#     )
#     await state.set_state(GetKey.key)
#
#
# @router.callback_query(F.data.startswith("get_key_"))
# async def you_key(callback_query: types.CallbackQuery,
#                   state: FSMContext,
#                   user):
#     access_url, text = await service.get_vpn_key(user.telegram_id, callback_query)
#
#     await callback_query.message.edit_text(text, parse_mode="HTML")
#     await callback_query.message.answer(f'`{access_url}`', parse_mode='MarkdownV2')
#
#     await state.clear()

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
