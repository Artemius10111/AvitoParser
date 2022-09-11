import logging
import os
from datetime import datetime 

def file_name_datetime() -> str:
    """
    Возврощает корректное название для файла логов
    """
    return str(datetime.now().strftime("%D:%H:%M:%S")).replace('/', ':').replace(':', '_')

def create_file_to_logger() -> None:
    """
    Создает файл для логов
    """
    with open(f'ParserScripts/Results/Logs/{file_name_datetime()}', 'a') as file: pass

def get_logger() -> logging.getLogger():
    """
    Возвращает логгер как объект
    """
    create_file_to_logger()
    logging.basicConfig(filename=f'ParserScripts/Results/Logs/{file_name_datetime()}', encoding='utf-8', level=logging.INFO)
    LOGGER = logging.getLogger(__name__)
    return LOGGER

