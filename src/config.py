import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class VpnConfig:
    api_url: str
    cert_sha256: str


vpn_config = {
    "poland": VpnConfig(
        api_url=os.environ.get("API_URL_POLAND"),
        cert_sha256=os.environ.get("CERT_SHA256_POLAND")
    ),
    "germany": VpnConfig(
        api_url=os.environ.get("API_URL_GERMANY"),
        cert_sha256=os.environ.get("CERT_SHA256_GERMANY")
    )}


@dataclass
class BotToken:
    access_token: str


bot_token = BotToken(access_token=os.environ.get("BOT_TOKEN"))


@dataclass
class DBConfig:
    host: str
    port: str
    name: str
    user: str
    password: str


dbconfig = DBConfig(
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT"),
    name=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS")
)


@dataclass
class RedisConfig:
    host: str
    port: str


redis_config = RedisConfig(
    host=os.environ.get("REDIS_HOST"),
    port=os.environ.get("REDIS_PORT")
)


@dataclass
class CeleryConfig:
    broker: str
    backend: str


celery_config = CeleryConfig(
    broker=f'redis://{redis_config.host}:{redis_config.port}/0',
    backend=f'redis://{redis_config.host}:{redis_config.port}/0'
)
