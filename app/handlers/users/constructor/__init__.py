from aiogram import Dispatcher
from loguru import logger

from .client import (
    stop_constructor, start_constructor, save_main_image, save_text_image, get_text_position_on_image,
    other_message_handler, get_filters
)


def setup_constructor_handlers(dp: Dispatcher):
    # dp.register_message_handler(stop_constructor, commands=['stop'], state='*')
    # dp.register_message_handler(start_constructor, commands=['create'])
    # dp.register_message_handler(save_background_image, state=ConstructorSG.get_back_image,
    #                             content_types=['document', 'photo'])
    # dp.register_message_handler(save_text_image, state=ConstructorSG.get_text_image,
    #                             content_types=['document'])
    # dp.register_message_handler(get_text_position_on_image, text_equals=position_buttons,
    #                             state=ConstructorSG.get_position)
    # dp.register_message_handler(other_message_handler, state=ConstructorSG)

    dp.register_message_handler(stop_constructor, **get_filters(stop_constructor))
    dp.register_message_handler(start_constructor, **get_filters(start_constructor))
    dp.register_message_handler(save_main_image, **get_filters(save_main_image))
    dp.register_message_handler(save_text_image, **get_filters(save_text_image))
    dp.register_message_handler(get_text_position_on_image, **get_filters(get_text_position_on_image))
    dp.register_message_handler(other_message_handler, **get_filters(other_message_handler))

    logger.info('Constructor handlers are successfully configured')
