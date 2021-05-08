from aiogram.contrib.middlewares.fsm import FSMSStorageProxy
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from app.states import ConstructorSG
from . import server_response, services


async def stop_constructor(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer('Остановлено', reply_markup=ReplyKeyboardRemove())


async def start_constructor(msg: Message):
    await ConstructorSG.get_background_image.set()

    return await msg.answer(services.START_TEXT)

    await Constructor.get_background_image.set()


    state_data['background_image'] = image
    await msg.answer(
        'Отлично! \nТеперь отправьте фотографию с отыгровками на черном фоне, '
        'таким же образом.'
    )
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
