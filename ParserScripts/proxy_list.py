

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
