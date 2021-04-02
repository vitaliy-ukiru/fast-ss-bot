from aiogram import Dispatcher
from aiogram.types import BotCommand
from loguru import logger

from app.config import BOT_COMMANDS


async def setup_bot_commands(dp: Dispatcher) -> None:
    commands = [BotCommand(name, desc) for name, desc in BOT_COMMANDS.items()]
    await dp.bot.set_my_commands(commands)
    logger.info('Bot commands are successfully configured')
