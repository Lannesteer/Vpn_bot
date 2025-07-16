from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.handlers.users.start.text import StartButtons
from src.handlers.users.vpn.text import VpnButton, VpnTexts


class GetKeysCallBack(CallbackData, prefix="VpnKeys"):
    action: str


class ChooseCountryCallback(CallbackData, prefix="VpnCountry"):
    country: str


class ChooseServerCallback(CallbackData, prefix="VpnServer"):
    server: str


class ServerInfoCallback(CallbackData, prefix="VpnServerInfo"):
    action: str


def keys_kb(get_key=False,
            keys=None,
            countries=None,
            servers=None,
            server_info=None):
    builder = InlineKeyboardBuilder()
    if get_key:
        builder.button(
            text=VpnButton.GetKey,
            callback_data=GetKeysCallBack(
                action="get_key"
            )
        )
    if keys:
        for key in keys:
            builder.button(
                text=f"{key.server.country}, 100GB, {key.server.price}₽/месяц",
                callback_data=f'Key{key.id}'
            )
    elif countries:
        for country in countries:
            builder.button(
                text=country.country,
                callback_data=ChooseCountryCallback(
                    country=country.country
                )
            )
    elif servers:
        for server in servers:
            builder.button(
                text=f"{server.country}, 100GB, {server.price}₽/месяц",
                callback_data=ChooseServerCallback(
                    server=server.country
                )
            )
    elif server_info:
        builder.button(
            text=VpnButton.GetKey2,
            callback_data=ServerInfoCallback(action="get_key"))

    builder.button(text=VpnButton.Cancel, callback_data="cancel") if server_info \
        else builder.button(text=StartButtons.CancelButton, callback_data="cancel")

    builder.adjust(1)

    return builder.as_markup()


@dataclass
class VpnCallbacks:
    KeysCB = GetKeysCallBack
    CountryCB = ChooseCountryCallback
    ServersCB = ChooseServerCallback
    ServerInfoCB = ServerInfoCallback


@dataclass
class VpnKeyboardsCallBacks:
    Keys = keys_kb