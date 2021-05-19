from aiogram.utils import markdown as md

from app.config import BOT_COMMANDS, PIN_ADMIN, GITHUB_REPO

START_TEXT = 'Привет! Перед работай со мной почитай /about и /help. Там вся ' \
             'информация'

commands = [f'/{name} - {md.hcode(desc)}\n' for name, desc in BOT_COMMANDS.items()]

HELP_TEXT = f"""
<code>Команды бота</code>
{''.join(commands)}

<code>Руководство по конструктору</code>
Запустить конструктор командой /create.
Картинки загружать надо как документ (параметр 'без сжатия' в десктоп клиенте). \
Иначе клиент телеграма сжимает их, а это прямо влияет на работу бота.
О найденных багах пишите на контактную информацию из /about
"""

ABOUT_TEXT = md.text(
    'Данный проект - всего лишь эксперимент, сделанный от скуки и только интереса ради',
    'Если вы нашли баг, ошибку или у вас есть предложение - пишите мне в ПМ или репозитории проекта.\n',
    f'Телеграм разработчика - {PIN_ADMIN}',
    f'Исходный код - {md.hlink("репозиторий GitHub", GITHUB_REPO)}.',
    sep='\n'
)

START_CONSTRUCTOR_TEXT = md.text(
    md.hcode('Вы запустили конструктор сс.\n'),
    'Отправьте мне изображение которое будет задним фоном.',
    md.hbold('Важно! Отправить нужно документом (без сжатия), а не фоткой!'),
    sep='\n'
)

USER_ERROR_TEXT = md.text(
    'Произошла ошибка. Скорее всего картинка с отыгровками сжата',
    'Я отправил отчёт администратору ({})'.format(PIN_ADMIN),
    sep='\n'
)


def admin_error_text(error: Exception, mention: str, chat_id: int):
    return md.text(
        md.text(md.hbold('[Ошибка]'), '|', md.hcode(error), '|'),
        md.text('Chat:', md.text(mention), '|', md.hcode(chat_id))
    )
