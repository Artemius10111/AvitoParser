from cgitb import text
from typing import Iterable
from aiohttp import ClientSession
import asyncio
import xmltodict
import json
from functions.logger import get_logger
from datetime import date, datetime
LOGGER = get_logger()


async def get_areas() -> None:
    """
    Сохраняет все города, представленные авито, в файл json
    """
    LOGGER.info(f"Функция get_areas была запущена в {datetime.now()}")
    async with ClientSession() as session:
        async with session.get("https://autoload.avito.ru/format/DisplayAreas.xml") as resp:
            if resp.status == 200:
                text_xml = await resp.text()
                areas_dict = xmltodict.parse(text_xml)
                with open('Results/areas.json', 'w', encoding='utf-8') as file:
                    file.write(json.dumps(areas_dict))
            

def serialize_data_areas() -> Iterable:
    """
    Возвращает словарь всех городов из json файла
    """
    LOGGER.info(f"Функция serialize_data_areas была запущена в {datetime.now()}")
    with open('ParserScripts/Results/areas.json', 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
        return [list(i.values()) for i in data.values()][0][0]

