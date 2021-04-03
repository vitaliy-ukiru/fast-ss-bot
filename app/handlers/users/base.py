from aiogram import types

from app.service.texts import START_TEXT, HELP_TEXT
from app.utils.notify_admin import on_start_cmd_notify


async def start_command(msg: types.Message) -> types.Message:
    await on_start_cmd_notify(msg.bot, msg.from_user)
    return await msg.answer(START_TEXT)


async def help_command(msg: types.Message) -> types.Message:
    return await msg.answer(HELP_TEXT)
