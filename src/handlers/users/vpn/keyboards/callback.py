from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.handlers.users.start.text import StartButtons
from src.handlers.users.vpn.text import VpnButton


class KeysCallBack(CallbackData, prefix="Vpn"):
    action: str


def keys_kb(keys=None):
    builder = InlineKeyboardBuilder()

    builder.button(
        text=VpnButton.GetKey,
        callback_data=KeysCallBack(
            action="get_key"
        )
    )
    if keys:
        for key in keys:
            builder.button(
                text=f"{key.server.country},100GB,{key.server.price}₽/месяц.",
                callback_data=f'Key{key.id}'
            )

    builder.button(text=StartButtons.CancelButton, callback_data="cancel")

    builder.adjust(1)

    return builder.as_markup()


@dataclass
class VpnCallbacks:
    KeysCB = KeysCallBack


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
