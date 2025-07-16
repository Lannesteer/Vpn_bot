import asyncio
import platform
import re

from aiogram import Bot


class VpnUtils:
    @staticmethod
    async def get_ping(ip: str) -> float:
        """Функция проверяет пинг до сервера и возвращает его в миллисекундах"""
        try:
            param = "-n" if platform.system().lower() == "windows" else "-c"
            process = await asyncio.create_subprocess_exec(
                "ping", param, "1", ip,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            encoding = "cp866" if platform.system().lower() == "windows" else "utf-8"
            output = stdout.decode(encoding, errors="ignore")  # Указываем кодировку

            # Для Windows ищем "время=XXмс" (или "Среднее = XX мсек" в статистике)
            match_win = re.search(r"время=(\d+)мс", output)
            match_avg = re.search(r"Среднее = (\d+) мсек", output)

            if match_win:
                return float(match_win.group(1))
            elif match_avg:
                return float(match_avg.group(1))
            else:
                return -1  # Ошибка в получении пинга

        except Exception as e:
            print(f"Ошибка при проверке пинга: {e}")
            return -1

    @staticmethod
    async def gb_limit_converter(key):
        if key.data_limit is not None:
            gb_limit = round(key.data_limit / (1024 ** 3))
            return gb_limit

    @staticmethod
    async def notify_users(bot: Bot, telegram_id, text, reply_markup=None, parse_mode=None):
        await bot.send_message(chat_id=telegram_id,
                               text=text,
                               reply_markup=reply_markup,
                               parse_mode=parse_mode)


vpn_utils = VpnUtils()

# async def get_ping(host: str) -> float:
#     """Проверяет пинг к серверу (возвращает ms или -1, если ошибка)"""
#
#     param = "-n" if platform.system().lower() == "windows" else "-c"
#     try:
#         result = await asyncio.create_subprocess_exec(
#             "ping", param, "1", host,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         stdout, _ = await result.communicate()
#
#         output = stdout.decode()
#         if "time=" in output:
#             time_ms = output.split("time=")[-1].split(" ")[0]
#             return float(time_ms)
#         return -1
#     except Exception:
#         return -1
