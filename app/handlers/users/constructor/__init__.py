__all__ = ['setup_handlers']

from aiogram import Dispatcher
from loguru import logger

from .client import (
    stop_constructor, start_constructor, save_main_image, save_text_image, get_text_position_on_image,
    other_message_handler, setup_handler
)


def setup_handlers(dp: Dispatcher):
    dp.register_message_handler(**setup_handler(stop_constructor))
    dp.register_message_handler(**setup_handler(start_constructor))
    dp.register_message_handler(**setup_handler(save_main_image))
    dp.register_message_handler(**setup_handler(save_text_image))
    dp.register_message_handler(**setup_handler(get_text_position_on_image))
    dp.register_message_handler(**setup_handler(other_message_handler))

    logger.info('Constructor handlers are successfully configured')
