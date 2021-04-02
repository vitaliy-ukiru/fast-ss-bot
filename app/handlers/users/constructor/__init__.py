from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from loguru import logger

from app.config import position_buttons
from app.states.screenshot_situation_states import Constructor
from .client import (stop_constructor, start_constructor, save_background_image,
                     save_text_image, get_text_position_on_image,
                     other_message_handler)


def setup_constructor_handlers(dp: Dispatcher):
    dp.register_message_handler(stop_constructor, commands=['stop'], state='*')
    dp.register_message_handler(start_constructor, commands=['create'])
    dp.register_message_handler(save_background_image,
                                state=Constructor.get_background_image,
                                content_types=['document', 'photo'])
    dp.register_message_handler(save_text_image,
                                state=Constructor.get_text_image,
                                content_types=['document'])
    dp.register_message_handler(get_text_position_on_image,
                                Text(equals=position_buttons),
                                state=Constructor.get_position)
    dp.register_message_handler(other_message_handler, state=Constructor)

    logger.info('Constructor handlers are successfully configured')
