from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int, ...] = (1, 1),
):
    keyboard = InlineKeyboardBuilder()

    # btns['❌ Закрыть меню'] = 'close_menu'

    for text, data in btns.items():

        if isinstance(text, tuple):
            keyboard.add(InlineKeyboardButton(
                text=", ".join(str(item) for item in text[1:] if item is not None),
                callback_data=data)
            )
        else:
            keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboard.adjust(*sizes).as_markup()


country_btns = {
    "Польша 🇵🇱": 'country_poland',
    "Германия 🇩🇪": 'country_germany'
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
