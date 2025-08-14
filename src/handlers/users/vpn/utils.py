import asyncio
import platform
import re

import requests

from src.config import BotConfig


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
    def bytes_limit_converter(limit):
        if limit:
            mb = limit / 1024 / 1024
            if mb < 1024:
                return f"{mb:.2f} МБ"
            gb = mb / 1024
            return f"{gb:.2f} ГБ"
        else:
            return "n/a"

    @staticmethod
    def notify_users_from_celery(telegram_id, text, reply_markup=None, parse_mode=None):
        url = f"https://api.telegram.org/bot{BotConfig.access_token}/sendMessage"
        payload = {
            "chat_id": telegram_id,
            "text": text
        }
        if reply_markup:
            payload["reply_markup"] = reply_markup
        if parse_mode:
            payload["parse_mode"] = parse_mode

        requests.post(url, json=payload)


vpn_utils = VpnUtils()
