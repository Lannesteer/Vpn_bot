# import asyncio
#
# from src.bot.schemas import UserUpdate
# from src.database import get_service



# def check_balance(user_id: str, key_id: int):
#     from src.bot.service import UserService, KeyService
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     print('задача запущена')
#
#     async def async_task():
#         print('задача запущена')
#         session = await get_service(KeyService)
#         key_service = KeyService(session)
#
#         session_user = await get_service(UserService)
#         user_service = UserService(session_user)
#
#         user = await user_service.get_one(user_id)
#
#         if user and user.balance < 200:
#             await key_service.delete(key_id)
#             print(f"❌ Ключ {key_id} удален у пользователя {user_id} из-за нехватки средств.")
#         else:
#             data = UserUpdate(balance=user.balance - 200)
#             await user_service.update(data, user_id)
#             print(f"💰 У пользователя {user_id} списано 200 ₽ за продление ключа.")
#
#     loop.run_until_complete(async_task())
#     loop.close()
