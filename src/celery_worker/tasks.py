# import asyncio
#
# from src.database.users.schemas import UserUpdate
# from src.celery_worker.celery_worker import celery_app
#
#
# @celery_app.task
# def check_balance(user_id: str, key_id: int):
#     """
#     Проверяет баланс пользователя и удаляет ключ, если недостаточно средств.
#     """
#
#     async def async_task():
#
#         user = await user_service.get_one(user_id)
#         if not user:
#             return
#
#         if user.balance < 200:
#             await key_service.delete(key_id)
#             print(f"❌ Ключ {key_id} удален у пользователя {user_id} из-за нехватки средств.")
#         else:
#             data = UserUpdate(balance=user.balance - 200)
#             await user_service.update(data, user_id)
#
#     asyncio.run(async_task())
