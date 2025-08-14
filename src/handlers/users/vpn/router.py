from aiogram import types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database.keys.service import key_service
from services.outline.manager import outline_manager
from src.config import vpn_config
from src.database.servers.service import server_service
from src.database.users.service import user_service
from .keyboards.callback import VpnKeyboardsCallBacks, VpnCallbacks
from aiogram import Router

from .service import vpn_service
from .state import VpvState
from .text import VpnTexts
from .utils import vpn_utils
from ..start.text import StartButtons

router = Router()


@router.message(StateFilter('*'), F.text == StartButtons.KeysButton)
async def get_user_keys(message: types.Message,
                        user):
    user_keys = await user_service.get_all_user_keys(user.id)
    await message.answer(
        text=VpnTexts.UserKeys,
        reply_markup=VpnKeyboardsCallBacks.Keys(get_key=True, keys=user_keys)
    )


@router.callback_query(VpnCallbacks.KeysCB.filter(), StateFilter('*'))
async def get_key(call: CallbackQuery, callback_data: VpnCallbacks.KeysCB, state: FSMContext):
    if callback_data.action == "get_key":
        countries = await server_service.all()
        await call.message.edit_text(
            VpnTexts.ServerLocation,
            reply_markup=VpnKeyboardsCallBacks.Keys(countries=countries)
        )
        await state.set_state(VpvState.ChooseCountry)


@router.callback_query(VpnCallbacks.CountryCB.filter(), StateFilter('*'))
async def select_country(call: CallbackQuery,
                         callback_data: VpnCallbacks.CountryCB,
                         state: FSMContext):
    await state.update_data(country=callback_data.country)
    servers = await server_service.get_servers_by_country(country=callback_data.country)
    await call.message.edit_text(
        text=VpnTexts.SelectServer,
        reply_markup=VpnKeyboardsCallBacks.Keys(servers=servers)
    )
    await state.set_state(VpvState.ChooseServer)


@router.callback_query(VpnCallbacks.ServersCB.filter(), StateFilter(VpvState.ChooseServer))
async def select_server(call: types.CallbackQuery,
                        callback_data: VpnCallbacks.ServersCB,
                        state: FSMContext):
    server = await server_service.get_server_by_country(callback_data.server)
    ip_server = vpn_config.get(f'{callback_data.server}').api
    ping = await vpn_utils.get_ping(ip_server)
    await call.message.edit_text(
        text=VpnTexts.ServerInfo.format(
            Server=f"{server.country}, 100GB, {server.price}₽/месяц",
            Type=server.type,
            Country=server.country,
            Ping=ping,
            Price=server.price
        ),
        reply_markup=VpnKeyboardsCallBacks.Keys(server_info=True)
    )


@router.callback_query(VpnCallbacks.ServerInfoCB.filter(), StateFilter(VpvState.ChooseServer))
async def server_info_get_key(call: CallbackQuery,
                              callback_data: VpnCallbacks.ServerInfoCB,
                              state: FSMContext,
                              user):
    data = await state.get_data()
    country = data.get("country")
    if callback_data.action == "get_key":
        server = await server_service.get_server_by_country(country)
        vpn_key = await vpn_service.configurate_vpn_key(server, user)
        await call.message.delete()
        await call.message.answer(text=VpnTexts.KeyDone.format(Price=server.price))
        await call.message.answer(text=f'`{vpn_key}`', parse_mode="MarkdownV2")
        await state.clear()


@router.callback_query(VpnCallbacks.KeyInfoCB.filter(), StateFilter("*"))
async def key_info(call: CallbackQuery, callback_data: VpnCallbacks.KeyInfoCB):
    key = await key_service.get_key(callback_data.key_id)
    text = None
    if callback_data.key_id:
        vpn_client = await outline_manager.vpn_client_init(key.server)
        used_limit = vpn_utils.bytes_limit_converter(
            vpn_client.get_key(str(key.id)).used_bytes
        )
        text = VpnTexts.KeyInfo.format(
            Key=f"{key.server.country}, 100GB, {key.server.price}₽/месяц",
            Date=key.created_at.replace(microsecond=0),
            ExpiryDate=key.expiry_date.replace(microsecond=0),
            UsedData=used_limit
        )
    elif callback_data.actions == "show_key":
        text = None
    elif callback_data.actions == "delete_key":
        text = ""

    await call.message.edit_text(
        text=text,
        reply_markup=VpnKeyboardsCallBacks.Keys(key_info=True)
    )
