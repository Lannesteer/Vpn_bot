from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.handlers.admins.servers.text import ServerButtons
from src.handlers.users.start.text import StartButtons


class ServersControlCallback(CallbackData, prefix="UserControl"):
    action: str


def servers_kb(add=False,
               confirm=False):
    builder = InlineKeyboardBuilder()

    if add:
        builder.button(
            text=ServerButtons.AddServer,
            callback_data=ServersControlCallback(
                action="add_server"
            )
        )
        builder.button(
            text=ServerButtons.RemoveServer,
            callback_data=ServersControlCallback(
                action="remove_server"
            )
        )
    elif confirm:
        builder.button(
            text=ServerButtons.Confirm,
            callback_data=ServersControlCallback(
                action="confirm"
            )
        )
    builder.button(text=StartButtons.CancelButton, callback_data="cancel")

    builder.adjust(1, 1)

    return builder.as_markup()


@dataclass
class ServersCallBacks:
    ServersCB = ServersControlCallback


@dataclass
class ServersKeyboardsCallBacks:
    ServersControl = servers_kb
