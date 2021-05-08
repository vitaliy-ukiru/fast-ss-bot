from aiogram import types

from app.keyboards import contact_urls
from app.service.texts import ABOUT_TEXT


async def about_command(msg: types.Message):
    return await msg.answer(ABOUT_TEXT, reply_markup=contact_urls())
