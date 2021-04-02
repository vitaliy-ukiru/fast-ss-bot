import logging

from aiogram.dispatcher.handler import SkipHandler
from aiogram.utils.exceptions import (
    Unauthorized, InvalidQueryID, MessageNotModified, MessageToDeleteNotFound,
    MessageTextIsEmpty, RetryAfter, CantParseEntities, MessageCantBeDeleted
)


async def process_errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        logging.warning('Message is not modified')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.warning('Message cant be deleted')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.warning('Message to delete not found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.warning('MessageTextIsEmpty')
        return True

    if isinstance(exception, Unauthorized):
        logging.warning(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.warning(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, RetryAfter):
        logging.warning(f'RetryAfter: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.warning(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, SkipHandler):
        return True

    logging.info(f'Exception update: {update} \n{exception}')
