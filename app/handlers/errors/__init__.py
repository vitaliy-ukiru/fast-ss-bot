from aiogram import Dispatcher
from loguru import logger

from .errors_handler import process_errors_handler


def setup_handlers(dp: Dispatcher):
    dp.register_errors_handler(process_errors_handler)
    logger.info('Error handlers are successfully configured')
