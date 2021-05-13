from aiogram.contrib.middlewares.fsm import FSMSStorageProxy
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from app.config import position_buttons
from app.states import ConstructorSG
from . import server_response, services


async def stop_constructor(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer('Остановлено', reply_markup=ReplyKeyboardRemove())


async def start_constructor(msg: Message):
    await ConstructorSG.get_back_image.set()
    return await msg.answer(services.START_TEXT)


async def save_main_image(msg: Message, state_data: FSMSStorageProxy):
    image = services.get_picture(msg)
    if not image:
        return await msg.answer('Ты мне отправил не картинку.')

    state_data['background_image'] = image
    await msg.answer('Отлично!\n'
                     'Теперь отправьте фотографию с отыгровками на черном фоне, таким же образом.')
    await ConstructorSG.next()


async def save_text_image(msg: Message, state_data: FSMSStorageProxy):
    document = services.get_picture(msg)
    if not document:
        return await msg.answer('Нужно отправить картинку как документ!')

    state_data['text_image'] = document
    await ConstructorSG.next()

    return await msg.answer('Где расположить текст?', reply_markup=services.position_keyboard())


async def get_text_position_on_image(msg: Message, state_data: FSMSStorageProxy):
    state_data['text_position'] = services.get_position(msg.text)
    await msg.answer('Начинаю обрабатывать фотографию.', reply_markup=ReplyKeyboardRemove())
    return await server_response.create_image(msg, state_data)


async def other_message_handler(msg: Message):
    return await msg.answer('Если ты видишь это сообщение, значит что-то делаешь не так.')


FILTERS = {
    'stop_constructor': {'commands': 'stop', 'state': '*'},
    'start_constructor': {'commands': 'create'},
    'save_main_image': {'state': ConstructorSG.get_back_image, 'content_types': ['document', 'photo']},
    'save_text_image': {'state': ConstructorSG.get_text_image, 'content_types': 'document'},
    'get_text_position_on_image': {'text': position_buttons, 'state': ConstructorSG.get_position},
    'other_message_handler': {'state': ConstructorSG}
}


def get_filters(func):
    return FILTERS[str(func)]
