# файл с конфигурационными данными для бота, базы данных, сторонних сервисов и тд

from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str       # название базы данных
    db_host: str        # URL-адрес базы данных
    db_user: str        # имя пользователя базы данных
    db_password: str    # пароль к базе данных

@dataclass
class TgBot:
    token: str              # токен бота
    admin_ids: list[int]    # список id администраторов бота

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig



# create function for creating object of config

def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db = DatabaseConfig(
            database = env('DATABASE'),
            db_host = env('DB_HOST'),
            db_user = env('DB_USER'),
            db_password = env('DB_PASSWORD')
        )
    )

