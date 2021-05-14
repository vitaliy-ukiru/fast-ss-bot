from aiogram import Dispatcher
from loguru import logger

from . import errors, users


def setup(dp: Dispatcher):
    users.setup_handlers(dp)
    errors.setup_handlers(dp)
    logger.info('\u001b[1;92m Handlers are successfully configured\u001b[0m')
