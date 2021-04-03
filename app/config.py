from pathlib import Path

from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN_ID = env.int("ADMIN_ID")
ADMIN_USERNAME = env.str("ADMIN_USERNAME")
PIN_ADMIN = f'@{ADMIN_USERNAME}'
GITHUB_REPO = 'https://github.com/vitaliy-ukiru/fast-ss-bot'
WORK_PATH: Path = Path(__file__).parent.parent


position_buttons = ["Сверху", "Снизу"]
BOT_COMMANDS = {
    'help': 'Справка по боту',
    'create': 'Создать сс',
    'stop': 'Остановить процесс создания сс',
    'about': 'Инфорация о боте'
}
