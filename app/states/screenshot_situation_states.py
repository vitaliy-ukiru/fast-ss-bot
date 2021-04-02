from aiogram.dispatcher.filters.state import StatesGroup, State


class Constructor(StatesGroup):
    get_background_image = State()
    get_text_image = State()
    get_position = State()
