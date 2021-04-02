from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.utils.markdown import hbold, hcode
from loguru import logger

from app.config import position_buttons
from app.states.screenshot_situation_states import Constructor
from .server_response import create_image


async def stop_constructor(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('Остановлено', reply_markup=types.ReplyKeyboardRemove())


async def start_constructor(msg: types.Message):

    await msg.answer('\n'.join([
        hcode('Вы запустили конструктор сс.\n'),
        'Отправьте мне изображение которое будет задним фоном.',
        hbold('Важно! Отправить нужно документом (без сжатия), а не фоткой!')
        ]))

    await Constructor.get_background_image.set()


async def save_background_image(msg: types.Message, state: FSMContext):
    content_type = msg.content_type
    if content_type == 'photo':
        image = msg.photo[-1]
    elif content_type == 'document' and msg.document.mime_base == 'image':
        image = msg.document
    else:
        logger.debug('Invalid document/photo' + str(msg))
        return await msg.answer('Ты мне чето-то не то отправил')

    await state.update_data(background_image=image)
    await msg.answer(
        'Отлично! \nТеперь отправьте фотографию с отыгровками на черном фоне, '
        'таким же образом.'
    )
    await Constructor.next()


async def save_text_image(msg: types.Message, state: FSMContext):
    document = msg.document
    if document.mime_base == 'image':
        await state.update_data(text_image=document)
    else:
        return await msg.answer('Нужно отправить картинку документом!')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*position_buttons)
    await msg.answer('Где расположить текст?',
                     reply_markup=markup)

    await Constructor.next()


async def get_text_position_on_image(msg: types.Message, state: FSMContext):
    # ["Сверху", "Снизу"]
    if msg.text == position_buttons[0]:
        position = 0
    elif msg.text == position_buttons[1]:
        position = 1
    else:
        position = 1

    await state.update_data(text_position=position)
    await msg.answer(
        'Начинаю обрабатывать фотогорафию.',
        reply_markup=types.ReplyKeyboardRemove()
    )
    await create_image(msg, state)


async def other_message_handler(msg: types.Message):
    await msg.answer('Если ты видишь это сообщение, значит что-то делаешь не так.')
