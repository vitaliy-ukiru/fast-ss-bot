from aiogram import Dispatcher
from loguru import logger

from app.handlers.users.constructor import setup_constructor_handlers
from .start import start_command


def user_handlers_setup(dp: Dispatcher):
    setup_constructor_handlers(dp)
    dp.register_message_handler(start_command, commands=['start'])
    logger.info('User handlers are successfully configured')
