from aiogram.dispatcher.filters.state import StatesGroup, State


class ConstructorSG(StatesGroup):
    get_back_image = State()
    get_text_image = State()
    get_position = State()
