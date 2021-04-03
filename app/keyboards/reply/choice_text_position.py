from aiogram.types import ReplyKeyboardMarkup

from app.config import position_buttons


def choice_text_position() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    return markup.add(*position_buttons)
