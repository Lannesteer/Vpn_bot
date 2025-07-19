import os
from dataclasses import dataclass
from pathlib import Path

import dotenv
from dotenv import load_dotenv
from environs import Env

load_dotenv()

WORK_PATH: Path = Path(__file__).parent.parent
config = dotenv.dotenv_values(WORK_PATH / 'dev.env')
dev = config.get("DEV", "") == "True"

env = Env()
env.read_env('dev.env' if dev else '.env')


@dataclass
class BotConfig:
    access_token = env.str("BOT_TOKEN")
    superusers_ids = list(map(int, env.list("SUPERUSER_IDS")))


@dataclass
class DbConfig:
    host = env.str("DB_HOST")
    port = env.str("DB_PORT")
    name = env.str("DB_NAME")
    user = env.str("DB_USER")
    password = env.str("DB_PASS")
    ssl = env.str("SSL_PATH")


@dataclass
class RedisConfig:
    host = env.str("REDIS_HOST")
    port = env.str("REDIS_PORT")
    password = env.str("REDIS_PASSWORD")
    redis_broker_url = env.str("REDIS_BROKER_URL")


@dataclass
class CeleryConfig:
    broker: str = f'redis://:{RedisConfig.password}@{RedisConfig.host}:{RedisConfig.port}/0'
    backend: str = f'redis://:{RedisConfig.password}@{RedisConfig.host}:{RedisConfig.port}/0'
    celery_queue = env.str("CELERY_QUEUE")


@dataclass
class VpnConfig:
    api: str
    api_url: str
    cert_sha256: str


vpn_config = {
    "🇵🇱 Польша": VpnConfig(
        api=os.environ.get("IP_POLAND"),
        api_url=os.environ.get("API_URL_POLAND"),
        cert_sha256=os.environ.get("CERT_SHA256_POLAND")
    ),
    "🇩🇪 Германия": VpnConfig(
        api=os.environ.get("IP_GERMANY"),
        api_url=os.environ.get("API_URL_GERMANY"),
        cert_sha256=os.environ.get("CERT_SHA256_GERMANY")
    )}
