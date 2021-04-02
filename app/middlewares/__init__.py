from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger


def middlewares_setup(dp: Dispatcher):
    dp.middleware.setup(LoggingMiddleware())
    logger.info('Middlewares are successfully configured')
