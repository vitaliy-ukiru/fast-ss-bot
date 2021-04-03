import atexit


from aiogram import Dispatcher
from aiogram.utils import executor
from loguru import logger

from app.handlers import handlers_setup
from app.loader import dp
from app.middlewares import middlewares_setup
from app import utils


async def on_startup(dispatcher: Dispatcher):
    handlers_setup(dispatcher)
    middlewares_setup(dispatcher)
    await utils.setup_bot_commands(dispatcher)
    await utils.on_startup_notify(dispatcher)
    logger.warning('\033[1;34m Bot is successfully configured \033[0m')


async def on_shutdown(dispatcher: Dispatcher):
    await dispatcher.bot.close()
    await utils.on_shutdown_notify(dispatcher)


def at_exit():
    logger.warning('\u001b[31;1m Stop program \u001b[0m')


if __name__ == '__main__':
    utils.setup_logger("INFO", ["aiogram.bot.api"])
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)

    atexit.register(at_exit)
