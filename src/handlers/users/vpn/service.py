import asyncio
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import types

from database.servers.service import server_service
from .keyboards.callback import servers_info
from database.base_class import BaseService
#
#
# class VpnService:
#     # async def get_servers_by_country(self, country: str):
#     #     servers = await server_service.get_servers_by_country(country)
#     #     servers_lst = []
#     #     for server in servers:
#     #         servers_lst .append(f'{server.country}, {server.price}')
#     #


#     async def get_user_keys(self, user):
#     #     user_keys = await user.keys
#     #
#
#     @staticmethod
#     async def get_servers_list(data: str):
#         server_name = data.split("_")[-1]
#         server_data = servers_info.get(server_name)
#
#         return {
#             f'{server_data["country"]} '
#             f'{server_data["country_flag"]}, '
#             f'100GB,{server_data["price"]}'
#             f'₽/месяц': f'server_info_{server_name}'
#         }
#
#     @staticmethod
#     async def get_server_info(data: str):
#         server_name = data.split("_")[-1]
#         server_data = servers_info.get(server_name)
#         server_ping = await get_ping(server_data.get('ip'))
#         text = (
#             f"🌍 <b>Информация о сервере {server_data['country_flag']} "
#             f"{server_data['country']}, 100GB, {server_data['price']}₽/месяц</b>\n\n"
#             f"🔹 <b>Тип:</b> {server_data['type']}\n"
#             f"⭐ <b>Рейтинг:</b> {server_data['rating']}\n"
#             f"📶 <b>Ping:</b> {server_ping} ms\n"
#             f"💰 <b>Стоимость:</b> {server_data['price']}₽/месяц.\n"
#             f"🎁 <b>Тестовый период:</b> {server_data['trial_period']}\n\n"
#             f"✅ Получая ключ, вы подтверждаете, что ознакомились и принимаете <a "
#             f"href='https://example.com/rules'>правила</a>."
#         )
#         get_key_btn = {"✅ Получить ключ": f"get_key_{server_name}"}
#
#         return text, get_key_btn
#
#     async def get_vpn_key(self,
#                           user_id,
#                           callback_query: types.CallbackQuery
#                           ):
#         server_name = (callback_query.data.split("_")[-1])
#         client = await get_vpn_clients(servers_info, server_name)
#
#         create_key = await client[server_name].create_key(key_name=str(user_id))
#         await client[server_name].add_data_limit(key_id=create_key.key_id, limit_bytes=1024 ** 3 * 100)
#
#         text = (
#             f"✅ *Вам выдан тестовый ключ на 30 мин*\n\n"
#             f"После истечения тестового периода будет предпринята попытка "
#             f"списать с вашего баланса стоимость ключа {servers_info[server_name]['price']}₽/месяц.\n"
#             f"Если списание не удастся, ключ будет *удален*!\n\n"
#             f"⚠ *Если ключ вам не подходит — удалите его, чтобы избежать списания средств!*\n\n"
#             f"*Ваш ключ:* ⬇️"
#         )
#         key = await client[server_name].get_key(create_key.key_id)
#
#         access_url = f'{key.access_url}&prefix=POST%20'
#
#         task = asyncio.create_task(
#             self.add_key_to_db(
#                 key.key_id,
#                 user_id,
#                 access_url
#             )
#         )
#
#         # check_balance.apply_async(args=[str(user_id), create_key.key_id], countdown=10)
#
#         return access_url, text
#
#     async def add_key_to_db(self,
#                             key_id: int,
#                             tg_user_id: int,
#                             access_url: str,
#                             ):
#         user = await self.get_one(str(tg_user_id))
#
#         if not user:
#             user_data = UserCreate(
#                 tg_user_id=str(tg_user_id)
#             )
#             await self.create(user_data)
#             user = await self.get_one(str(tg_user_id))
#
#             key_data = KeyCreate(
#                 id=key_id,
#                 access_url=access_url,
#                 user_id=user.id,
#                 expiry_date=(datetime.utcnow() + timedelta(days=30)).date()
#
#             )
#         else:
#             key_data = KeyCreate(
#                 id=key_id,
#                 access_url=access_url,
#                 user_id=user.id,
#                 expiry_date=(datetime.utcnow() + timedelta(days=30)).date()
#             )
#         await self.create(key_data)
#
#         return {"response": "success"}
#
#
vpn_service = VpnService()
