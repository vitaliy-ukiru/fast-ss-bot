from io import BytesIO
from typing import Union

from PIL import Image
from aiogram.contrib.middlewares.fsm import FSMSStorageProxy
from aiogram.types import Message, PhotoSize, Document

from app.service.paste_image import build_image
from app.service.texts import USER_ERROR_TEXT
from app.utils.notify_admin import error_notify


async def create_image(msg: Message, state: FSMSStorageProxy):
    await msg.answer_chat_action('upload_document')

    back: Union[PhotoSize, Document] = state['background_image']
    text: Document = state['text_image']
    text_position: int = state['text_position']

    with await back.download(BytesIO()) as background_im:
        with await text.download(BytesIO()) as text_im:
            main_img: Image.Image = Image.open(background_im).convert('RGBA')
            text_img: Image.Image = Image.open(text_im).convert('RGBA')

            try:
                final_img = build_image(main_img, text_img, text_position)
            except Exception as exp:
                await error_notify(msg, exp, document=text.file_id)

                return await msg.answer(USER_ERROR_TEXT)
            else:
                byte_io = BytesIO()
                byte_io.name = 'done.png'
                final_img.save(byte_io, 'PNG')
                byte_io.seek(0)

                await msg.answer_document(document=byte_io,
                                          caption='Готово')
            finally:
                return await state.fsm_context.finish()
