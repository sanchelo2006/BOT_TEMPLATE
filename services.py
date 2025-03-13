# модуль с реализацией бизнес логики
# временно перенесен в основную папку - когда все будет работать - надо замунуть обратно в папку service
# пока здесь прорабатываем логику проекта, после того как все настроим - этот комент будет удален!!!

# import Config class and func load_config from config.py
from config_data.config import Config, load_config
# TDClient main object of twelvedata
from twelvedata import TDClient
# pandas for easy working with data
import pandas as pd

# build congif object for load tokens and all settings (this is for main file!!!!)
config: Config = load_config()

# get api key for twelvedata (this is for main file!!!!)
api_key = config.tg_bot.api_key

# build object of twelvedata (this is for main file!!!!)
td = TDClient(apikey = api_key)

# function for get data from twelvedata
def get_data(symbol, interval):

     ts = td.time_series(
    symbol = symbol,
    interval = interval,
    outputsize=2)
     
     return ts


# function for get MACD cross 0
def get_MACD_change(ts, fast_period = 12, slow_period = 26, signal_period = 9):

    result_macd = '0'

    check_macd = ts.without_ohlc().with_macd(fast_period = fast_period,
                                            slow_period = slow_period,
                                            signal_period = signal_period).as_pandas()
    
    if check_macd['macd_hist'].iloc[1] > 0 and check_macd['macd_hist'].iloc[0] < 0:
        result_macd = 'MACD cross 0! UP > DOWN'

    elif check_macd['macd_hist'].iloc[1] < 0 and check_macd['macd_hist'].iloc[0] > 0:
        result_macd = 'MACD cross 0! DOWN > UP'

    return result_macd

# function for get RSC cross
def get_RSI(ts, time_period  =14):

    result_rsi = '0'

    check_rsi = ts.without_ohlc().with_rsi(time_period = time_period).as_pandas()

    if check_rsi['rsi'].iloc[1] > 40 and check_rsi['rsi'].iloc[0] < 40:
        result_rsi = 'RSI cross 40 DOWN > UP'
    
    elif check_rsi['rsi'].iloc[1] < 60 and check_rsi['rsi'].iloc[0] > 60:
        result_rsi = 'RSI cross 60 UP > DOWN'

    return result_rsi

# next code only for checking!!!!!!------------------
ts = get_data('BTC/USD', '1h')
check = get_MACD_change(ts)
check_rsi = get_RSI(ts)

print(check)
print(check_rsi)
#----------------------------------------------------