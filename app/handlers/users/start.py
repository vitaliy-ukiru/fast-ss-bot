from aiogram import types

from app.utils.notify_admin import on_start_cmd_notify


async def start_command(msg: types.Message) -> types.Message:
    await on_start_cmd_notify(msg.bot, msg.from_user)
    return await msg.answer('Привет! Для начала создания сс отправь мне ')
