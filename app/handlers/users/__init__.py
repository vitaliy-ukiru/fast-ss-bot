from aiogram import Dispatcher
from loguru import logger

from . import constructor
from .about import about_command
from .base import start_command, help_command


def setup_handlers(dp: Dispatcher):
    constructor.setup_handlers(dp)
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(about_command, commands=['about'])
    logger.info('User handlers are successfully configured')
