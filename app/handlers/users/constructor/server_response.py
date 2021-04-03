from io import BytesIO
from typing import Union

from PIL import Image
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, PhotoSize, Document

from app.config import PIN_ADMIN
from app.service.paste_image import build_image
from app.utils.notify_admin import error_notify


async def create_image(msg: Message, state: FSMContext):
    await msg.answer_chat_action('upload_document')

    data = await state.get_data()
    back: Union[PhotoSize, Document] = data['background_image']
    text: Document = data['text_image']
    text_position: int = data['text_position']

    with await back.download(BytesIO()) as background_im:
        with await text.download(BytesIO()) as text_im:
            main_img: Image.Image = Image.open(background_im).convert('RGBA')
            text_img: Image.Image = Image.open(text_im).convert('RGBA')

            try:
                final_img = build_image(main_img, text_img, text_position)
            except Exception as exp:
                await state.finish()
                await error_notify(msg, exp, document=text.file_id)

                return await msg.answer(
                    'Произошла ошибка. '
                    'Скорее всего картинка с отыгровками сжата.\n'
                    'Я отправил отчёт администратору ({})'.format(PIN_ADMIN)
                )
            else:
                byte_io = BytesIO()
                byte_io.name = 'done.png'
                final_img.save(byte_io, 'PNG')
                byte_io.seek(0)

                await msg.answer_document(document=byte_io,
                                          caption='Готово')

        await state.finish()
