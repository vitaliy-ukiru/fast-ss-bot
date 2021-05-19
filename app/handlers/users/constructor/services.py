__all__ = (
    'START_TEXT',
    'get_picture',
    'get_position',
    'position_keyboard'
)

from aiogram.types import Message

from app.config import position_buttons
from app.service.texts import START_CONSTRUCTOR_TEXT as START_TEXT
from app.keyboards import choice_text_position as position_keyboard


def get_picture(msg: Message):
    content_type = msg.content_type
    if content_type == 'photo':
        return msg.photo[-1]
    elif content_type == 'document' and msg.document.mime_base == 'image':
        return msg.document

    return False


def get_position(text: str):
    try:
        return position_buttons.index(text)
    except ValueError:
        return 1
