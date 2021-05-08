import logging

from aiogram import Dispatcher, Bot
from aiogram.types import Message, User

from app.config import ADMIN_ID
from app.service.texts import admin_error_text


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_ID, "Bot startup")

    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_ID, "Bot shutdown")
    except Exception as err:
        logging.exception(err)


async def on_start_cmd_notify(from_user: User) -> None:
    await send_to_admin(
        f'Use start command: {from_user.get_mention(as_html=True)} | {from_user.id}'
    )


async def send_to_admin(message_text: str) -> None:
    bot = Bot.get_current()
    await bot.send_message(ADMIN_ID, message_text)


async def error_notify(msg: Message, err, document):
    _text = admin_error_text(err, msg.from_user.get_mention('User', True), msg.chat.id)
    return await msg.bot.send_document(ADMIN_ID, document, caption=_text)
