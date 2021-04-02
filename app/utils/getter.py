import io

from aiogram import types
from PIL import Image


async def photo_getter(msg: types.Message):
    """
    Способ как можно получить картинку в байтовом потоке из сообщения.
    А так же отправка её в таком же виде.
    :param msg: Сообщение пользователя
    :return: Сообщение с изменной катинкой
    """
    photo = msg.photo[-1]

    with await photo.download(io.BytesIO()) as file:
        img: Image.Image = Image.open(file)

        # Некоторая работа с картинкой

        byte_io = io.BytesIO()
        byte_io.name = 'reply.png'
        img.save(byte_io, 'PNG')

        byte_io.seek(0)
        return await msg.answer_photo(photo=byte_io)
