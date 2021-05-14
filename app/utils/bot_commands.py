from aiogram import Dispatcher
from aiogram.types import BotCommand
from loguru import logger

from app.config import BOT_COMMANDS


async def setup_bot_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands([BotCommand(*cmd) for cmd in BOT_COMMANDS.items()])
    logger.info('Bot commands are successfully configured')
