from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.middlewares.fsm import FSMMiddleware
from loguru import logger


def setup(dp: Dispatcher):
    dp.middleware.setup_handlers(LoggingMiddleware())
    dp.middleware.setup_handlers(FSMMiddleware())
    logger.info('Middlewares are successfully configured')
