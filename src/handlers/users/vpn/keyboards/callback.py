from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.handlers.users.start.text import StartButtons
from src.handlers.users.vpn.text import VpnButton


class GetKeysCallBack(CallbackData, prefix="VpnKeys"):
    action: str


class ChooseCountryCallback(CallbackData, prefix="VpnCountry"):
    action: str


class ChooseServerCallback(CallbackData, prefix="VpnServer"):
    action: str


def keys_kb(get_key=False, keys=None, countries=None, servers=None):
    builder = InlineKeyboardBuilder()
    if get_key:
        builder.button(
            text=VpnButton.GetKey,
            callback_data=ChooseCountryCallback(
                action="get_key"
            )
        )
    elif keys:
        for key in keys:
            builder.button(
                text=f"{key.server.country}, 100GB, {key.server.price}₽/месяц",
                callback_data=f'Key{key.id}'
            )
    elif countries:
        for country in countries:
            builder.button(
                text=country.country,
                callback_data=ChooseServerCallback(
                    action=country.country
                )
            )
    elif servers:
        for server in servers:
            builder.button(
                text=f"{server.country}, 100GB, {server.price}₽/месяц",
                callback_data=ChooseServerCallback(
                    action=server.country
                )
            )

    builder.button(text=StartButtons.CancelButton, callback_data="cancel")

    builder.adjust(1)

    return builder.as_markup()


@dataclass
class VpnCallbacks:
    KeysCB = GetKeysCallBack
    CountryCB = ChooseCountryCallback
    ServersCB = ChooseServerCallback


@dataclass
class VpnKeyboardsCallBacks:
    Keys = keys_kb


country = {
    "Польша 🇵🇱": 'poland',
    "Германия 🇩🇪": 'germany'
}

servers_info = {
    "poland": {
        "id": 0,
        "country": "Польша",
        "ip": "91.239.148.249",
        "country_flag": "🇵🇱",
        "type": "🌐 Outline",
        "rating": "NA",
        "price": "200",
        "trial_period": "30 мин.",
    },
    "germany": {
        "id": 1,
        "country": "Германия",
        "ip": "185.140.12.144",
        "country_flag": "🇩🇪",
        "type": "🌐 Outline",
        "rating": "NA",
        "price": "200",
        "trial_period": "30 мин.",
    },
}
