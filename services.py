# модуль с реализацией бизнес логики
# временно перенесен в основную папку - когда все будет работать - надо замунуть обратно в папку service
# пока здесь прорабатываем логику проекта, после того как все настроим - этот комент будет удален!!!
# import Config class and func load_config from config.py
from config_data.config import Config, load_config
# TDClient main object of twelvedata
from twelvedata import TDClient

config: Config = load_config()

api_key = config.tg_bot.api_key


td = TDClient(apikey = api_key)

# Construct the necessary time series
ts = td.time_series(
    symbol="BTC/USD",
    interval="1h",
    outputsize=5
)

# Returns pandas.DataFrame
print(ts.with_macd().as_pandas())