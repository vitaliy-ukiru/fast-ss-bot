from aiogram import Dispatcher
from loguru import logger

from .users import user_handlers_setup
from .errors import errors_handlers_setup


def handlers_setup(dp: Dispatcher):
    user_handlers_setup(dp)
    errors_handlers_setup(dp)
    logger.info('\u001b[1;92m Handlers are successfully configured\u001b[0m')
