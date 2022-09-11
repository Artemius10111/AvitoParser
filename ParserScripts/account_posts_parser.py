import json
from unittest import FunctionTestCase
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
import os
import pandas as pd
import os
from datetime import date, datetime
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
ua = UserAgent()

from functions.logger import get_logger
LOGGER = get_logger()


class Account_Posts_Parser:
    """
    ____ ____ ____ ____ _  _ _  _ ___     ___  ____ ____ ___ ____     ___  ____ ____ ____ ____ ____ 
    |__| |    |    |  | |  | |\ |  |      |__] |  | [__   |  [__      |__] |__| |__/ [__  |___ |__/ 
    |  | |___ |___ |__| |__| | \|  |  ___ |    |__| ___]  |  ___] ___ |    |  | |  \ ___] |___ |  \ 
    """
    def __init__(self, link: str, parameters: Iterable) -> None:
        """
        Инициализируем класс парсера
        """
        self.parameters: Iterable = parameters
        self.__LINK: str = "https://www.avito.ru"
        self.__DEBUG = os.environ.get("DEBUG")
        self.__driver: webdriver.Chrome() = None
        self.login: str = ""
        self.password: str = ""

    def get_clear_browsing_button(self, driver):
        """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
        return driver.find_element(By.XPATH, '//*[@id="clearBrowsingDataConfirm"]')


    def clear_cache(self, driver, timeout=60):
        """Clear the cookies and cache for the ChromeDriver instance."""
        # navigate to the settings page
        driver.get('chrome://settings/clearBrowserData')

        # wait for the button to appear
        wait = WebDriverWait(driver, timeout)
        wait.until(self.get_clear_browsing_button)

        # click the button to clear the cache
        self.get_clear_browsing_button(driver).click()

        # wait for the button to be gone before returning
        wait.until_not(self.get_clear_browsing_button)


    def __configure_selenium(self) -> None:
        """
        Настраивает селениум для правильной работы
        """
        LOGGER.info(f"Функция __configure_selenium запущена {datetime.now()}")        
        options = webdriver.FirefoxOptions()
        print(user_agent := ua.firefox)
        options.add_argument(f"user-agent={user_agent}")
        options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\Firefox.exe'
        executable_path = os.environ['EXECUTABLE_PATH']
        driver = webdriver.Firefox(options=options, executable_path=executable_path)
        self.__driver: driver = driver

    def run(self):
        """
        Запуск
        """
        self.__configure_selenium()
        print(1)
        self.__driver.get(self.__LINK) 
        print(1)  
        time.sleep(self.parameters["wait_time"])
        self.login = self.get_data()[0]
        self.password = self.get_data()[1]
        print(1)
        self.__login()
        time.sleep(self.parameters["wait_time"])
        # self.__driver.close()    

    def get_data(self) -> Iterable:
        """
        Получает данные из файла excel
        """
        excel_data = pd.read_excel('data/input/posts_editor.xlsx')
        data = pd.DataFrame(excel_data)
        return (list(filter(lambda x: x !='',("".join((" ".join(str(data).split('\n0'))).split('  ')).split(' ')))))

    def __login(self):
        """
        Войти в аккаунт
        """
        self.__driver.find_element(By.XPATH, self.login_xpath()["menu_link"]).click()
        time.sleep(self.parameters["wait_time"])
        self.__driver.find_element(By.NAME, self.login_xpath()["login"]).send_keys(self.login)
        time.sleep(self.parameters["wait_time"])
        self.__driver.find_element(By.NAME, self.login_xpath()["password"]).send_keys(self.password)
        # Пора решить капчу!
        print(self.__driver.current_url)
        print("Пора решить капчу!")
        time.sleep(20000)

    def login_xpath(self) -> Mapping:
        """
        Возвращает ссылки xpath для логина в аккаунт
        """
        login_xpath_dict = {
            "menu_link": """//*[@id="app"]/div/div[1]/div/div/div/div[1]/div[2]/a""",
            "login": """login""",
            "password": """password""",
            "login_submit": """submit""",
        }
        return login_xpath_dict

    def kill(self):
        self.__driver.close() 

    def __make_click(self):
        self.__driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[5]/div/span/span/div').click()
        self.__driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[6]/div/div/span/div/div[1]/div[2]/div/input').send_keys("Щелково")
        time.sleep(10)
        