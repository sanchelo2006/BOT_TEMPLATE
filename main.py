# library for async functions
import asyncio
# library for logging
import logging

# import bot and dispathcer class
from aiogram import Bot, Dispatcher
# import ..........
from aiogram.client.default import DefaultBotProperties
# import .............
from aiogram.enums import ParseMode
# import Config class and func load_config from config.py
from config_data.config import Config, load_config

# import routers
# ...........
# import middleware
#............
# import support functions
# ...........

#init logger
logger = logging.getLogger(__name__)

# function for init and config of our bot
async def main():
    # config logging
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s [$(asctime)s] - %(name)s'
                               ' - %(message)s')

    # info to console about start bot
    logger.info('Starting bot')

    # load config
    config: Config = load_config()

    # init object of storage
    storage =  ...

    # init bot and dispatcher
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher(storage=storage)

    # init other objects (data base. cash etc)
    # ...

    # put objects in workflow of dispatcher
    dp.workflow_data.update(...)

    # register routers
    logger.info('connect routers')
    # ...

    # register middleware
    logger.info('connect middleware')
    # ...

    # pass collected updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())




