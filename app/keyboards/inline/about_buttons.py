from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.config import ADMIN_USERNAME, GITHUB_REPO


def contact_urls() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    return markup.add(
        InlineKeyboardButton('Telegram', url=f't.me/{ADMIN_USERNAME}'),
        InlineKeyboardButton('GitHub', url=GITHUB_REPO)
    )
