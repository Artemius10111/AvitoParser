import json
from pprint import pprint
from unittest import FunctionTestCase, result
from selenium import webdriver
import selenium.common.exceptions as exc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
from typing import (
    Iterable,
    Mapping,
)
import re
import os
from bs4 import BeautifulSoup
from datetime import date, datetime
import pandas as pd
from functions.logger import get_logger
LOGGER = get_logger()


class Search_Place_Parser:
    """
    ____ ____ ____ ____ ____ _  _     ___  _    ____ ____ ____     ___  ____ ____ ____ ____ ____ 
    [__  |___ |__| |__/ |    |__|     |__] |    |__| |    |___     |__] |__| |__/ [__  |___ |__/ 
    ___] |___ |  | |  \ |___ |  | ___ |    |___ |  | |___ |___ ___ |    |  | |  \ ___] |___ |  \                                                                                     
    """
    def __init__(self, parameters: Mapping) -> None:
        """
        Инициализируем класс парсера
        """
        self.city: str = ""
        self.parameters = parameters
        self.__LINK: str = "https://www.avito.ru"
        self.__FIGURED_RESPONSE_TEXT: str = '/schelkovo/zapchasti_i_aksessuary'
        self.__DEBUG = os.environ.get("DEBUG")
        self.__driver: webdriver.Chrome() = None


    def __configure_selenium(self) -> None:
        """
        Настраивает селениум для правильной работы
        """
        LOGGER.info(f"Функция __configure_selenium запущена {datetime.now()}")        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        # options.headless = True
        # options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        executable_path = os.environ['EXECUTABLE_PATH']
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
        self.__driver: driver = driver
        stealth(
                driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
        )
        # driver.get("https://www.youtube.com/")

    def run(self):
        """
        Запускает скрипт со всеми сценариями
        """
        LOGGER.info(f"Функция run запущена {datetime.now()}") 
        self.__configure_selenium()
        self.__driver.get(self.__LINK)   
        data = self.__get_data_excel()
        place_list = []
        for i in data:
            self.city = i[-2]
            self.__make_clicks_to_get_right_city()
            self.insert_value_to_search(i[-3])
            page_source = self.__driver.page_source
            place = self.parse_position(page_source, to_search=i[-1])
            place_list.append(place)
            self.__driver.get(self.__LINK)
        excel_data = pd.read_excel('data/input/places.xlsx')
        excel_data['places'] = excel_data.Series (place_list)
        # self.__only_name_choose()
        # time.sleep(self.parameters["wait_time"])
        # self.__make_clicks_to_get_category()
        # time.sleep(self.parameters["wait_time"])   

    def parse_position(self, page_source: str, to_search: str) -> Iterable:
        """
        Возвращает все названия аккаунтов по порядку расположения их объявлений
        """
        soup = BeautifulSoup(page_source, 'html.parser')
        elements = soup.find_all(attrs={"data-marker":"seller-rating"})
        elements = [(i.parent.parent.get('href')) for i in elements]
        elements = [to_search in i for i in elements]
        try:
            return elements.index(True) + 1
        except ValueError:
            return 0 
            



    def __get_data_excel(self) -> Iterable:
        """
        Получает данные из файла excel
        """
        excel_data = pd.read_excel('data/input/places.xlsx', index_col=0)
        excel_data_first = pd.read_excel('data/input/places.xlsx')
        data_first = pd.DataFrame(excel_data_first)
        data = pd.DataFrame(excel_data)
        list_data = (str(data).split("\n"))
        list_data_first = (str(data_first).split("\n"))
        list_data[0] = list_data_first[0]
        list_data.pop(1)
        result_list = list(map(lambda x: x.split('  '), list_data))
        return result_list

    def __make_clicks_to_get_right_city(self):
        """
        Делает клики для того, что бы получить правильный город
        """
        LOGGER.info(f"Функция __make_clicks_to_get_right_city запущена {datetime.now()}") 
        try:
            self.__driver.find_element(By.XPATH, self.city__xpath_of_elements()["city_choose"]).click()
            time.sleep(self.parameters["wait_time"])
            self.__driver.find_element(By.XPATH, self.city__xpath_of_elements()["send_form_city_choose"]).send_keys(self.city)
            time.sleep(self.parameters["wait_time"])
            self.__driver.find_element(By.XPATH, self.city__xpath_of_elements()["first_element_city_choose"]).click()
            time.sleep(self.parameters["wait_time"])
            self.__driver.find_element(By.XPATH, self.city__xpath_of_elements()["at_first_check_this_town's_posts"]).click()
            time.sleep(self.parameters["wait_time"])
            self.__driver.find_element(By.XPATH, self.city__xpath_of_elements()["confirm_city_choose"]).click()
        except Exception as e:
            print(e, flush=True)
            LOGGER.critical(f"Функция run была остановлена по причине ошибки {e} {datetime.now()}")

    def insert_value_to_search(self, value: str) -> None:
        """
        Вводит необходимые значения в поисковую форму
        """
        self.__driver.find_element(By.XPATH, self.search_xpath_of_elements()["search_label"]).send_keys(value)
        self.__driver.find_element(By.XPATH, self.search_xpath_of_elements()["find"]).click()

    def search_xpath_of_elements(self) -> Mapping:
        """
        Возвращает пути xpath поисковой формы
        """
        dict_ = {
            "search_label": """/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div/label[1]/input""",
            "find": """//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/button""",
        }
        return dict_

    def city__xpath_of_elements(self) -> Mapping:
        """
        Возвращает словарь на ссылки городов в формате xpath
        """
        LOGGER.info(f"Функция city__xpath_of_elements запущена {datetime.now()}") 
        dict_of_city_xpathes = {
            "city_choose": """//*[@id="app"]/div/div[2]/div/div[2]/div/div[5]/div[1]""",
            "first_element_city_choose": """//*[@id="app"]/div/div[2]/div/div[2]/div/div[6]/div/div/span/div/div[1]/div[2]/div/ul/li[1]""",
            "send_form_city_choose": """//*[@id="app"]/div/div[2]/div/div[2]/div/div[6]/div/div/span/div/div[1]/div[2]/div/input""",
            "at_first_check_this_town's_posts": """//*[@id="app"]/div/div[2]/div/div[2]/div/div[6]/div/div/span/div/div[3]/div/div[1]/label/span""",
            "confirm_city_choose": """//*[@id="app"]/div/div[2]/div/div[2]/div/div[6]/div/div/span/div/div[3]/div/div[2]/div/button"""
        }
        return dict_of_city_xpathes 