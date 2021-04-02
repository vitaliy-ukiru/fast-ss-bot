import logging

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.utils.markdown import hcode, hbold

from app.config import ADMIN_ID


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


async def on_start_cmd_notify(bot: Bot, from_user) -> None:
    await send_to_admin(
        bot,
        text=f'Use start command: @{from_user.username} | {from_user.id} | '
             f'{from_user.get_mention(as_html=True)}'
    )


async def send_to_admin(bot: Bot, text: str) -> None:
    await bot.send_message(ADMIN_ID, text)


async def error_notify(msg: Message, exp, document):
    await msg.bot.send_document(
        chat_id=ADMIN_ID, document=document,
        caption='\n'.join([
            f'{hbold("[Ошибка]")} | {hcode(exp)} |',
            'Chat: [{id}]. {user}'.format(
                id=msg.chat.id,
                user=msg.from_user.get_mention(name='User',
                                               as_html=True)
            )
        ])
    )
    return
