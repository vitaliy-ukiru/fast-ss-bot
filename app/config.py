import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
position_buttons = ["Сверху", "Снизу"]


BOT_COMMANDS = {
    'help': 'Справка по боту',
    'create': 'Создать сс',
    'stop': 'Остановить процесс создания сс',
    'about': 'Инфорация о боте'
}
