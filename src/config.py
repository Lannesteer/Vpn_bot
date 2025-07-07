import os
from dataclasses import dataclass

from dotenv import load_dotenv
from environs import Env

load_dotenv()

env = Env()
env.read_env('.env')


@dataclass
class BotToken:
    access_token = env.str("BOT_TOKEN")


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


@dataclass
class CeleryConfig:
    broker: str = f'redis://{RedisConfig.host}:{RedisConfig.port}/0'
    backend: str = f'redis://{RedisConfig.host}:{RedisConfig.port}/0'


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