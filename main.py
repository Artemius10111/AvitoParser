from multiprocessing.connection import wait
from typing import Mapping
from ParserScripts.avito_posts_parser import Avito_Posts_Parser
from ParserScripts.account_posts_parser import Account_Posts_Parser
from ParserScripts.search_place_parser import Search_Place_Parser
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6 import QtWidgets
from QtDesigns.PY.sample_3 import (
    Ui_MainWindow
)
from ParserScripts.areas import serialize_data_areas
from ParserScripts.categories import get_categories
import sys
app = QApplication(sys.argv)

class Main(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(Main, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Avito Parser")
        self.setFixedSize(self.width(), self.height())
        self.__connect_pages_to_buttons()
        self.__fill_list_view_with_cities()
        self.__fill_list_view_with_categories()

        self.__parser_buttons_connect()
        self.__parser_account_buttons_connect()
        self.__search_buttons_connect()
        self.__proxy_list_buttons_connect()
        self.__start_posts_edtior()

    def __connect_pages_to_buttons(self) -> None:
        """
        Соединяет кнопки со страницами
        """
        self.ui.ScrappingButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Scrapping_page))
        self.ui.SearchPositionButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Search_place_page))
        self.ui.ProxyListButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Proxy_list_page))
        self.ui.ImageEditorButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Image_Editor_page))
        self.ui.ScrappingAccountButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Scrapping_account_page))

    ######################################################################################################
    
    #   ____ _  _ _ ___ ____     ___  ____ ____ ___ ____     ___  ____ ____ ____ ____ ____ 
    #   |__| |  | |  |  |  |     |__] |  | [__   |  [__      |__] |__| |__/ [__  |___ |__/ 
    #   |  |  \/  |  |  |__| ___ |    |__| ___]  |  ___] ___ |    |  | |  \ ___] |___ |  \ 

    def __parser_buttons_connect(self) -> None:
        self.ui.ResultButton.clicked.connect(self.__result_parser)

    def __values_for_parser(self) -> Mapping:
        """
        Возвращает список значений всей страницы в качестве словаря
        """
        city = self.ui.AreasListWidget.currentItem().text()
        category = self.ui.CategoryListWidget.currentItem().text()
        name_only = self.ui.name_only_check_box.isChecked()
        title = self.ui.title_check_box.isChecked()
        description = self.ui.description_check_box.isChecked()
        views_num = self.ui.views_num_check_box.isChecked()
        datetime_ = self.ui.title_check_box.isChecked()
        paid_goods_used = self.ui.paid_goods_used_check_box.isChecked()
        price = self.ui.price_check_box.isChecked()
        url = self.ui.url_check_box.isChecked()
        wait_time = int(self.ui.wait_spin_box.text())
        num_pages = int(self.ui.depth_of_page_num_scrapping.text())
        final_dict = ({
            "city": city,
            "category": category,
            "name_only": name_only, 
            "title": title, 
            "description": description, 
            "views_num": views_num, 
            "datetime_": datetime_, 
            "paid_goods_used": paid_goods_used, 
            "price": price, 
            "url": url,
            "wait_time": wait_time,
            "num_pages": num_pages, 
            })
        return final_dict

    def __result_parser(self) -> None:
        final_dict = self.__values_for_parser()
        avito_parser = Avito_Posts_Parser(city=final_dict["city"], parameters=final_dict)
        avito_parser.run()
    
    def __fill_list_view_with_cities(self) -> None:
        """
        Берет города функцию get_areas из areas.py и наполняет ими list_view объект
        """
        self.ui.AreasListWidget.addItems(serialize_data_areas())

    def __fill_list_view_with_categories(self) -> None:
        """
        Берет категории из get_categories из categories.py и наполняет ими list_view объект
        """
        self.ui.CategoryListWidget.addItems(get_categories())
            
    #######################################################################################################

    #######################################################################################################
    #   ____ ____ ____ ____ _  _ _  _ ___     ___  ____ ____ ___ ____     ___  ____ ____ ____ ____ ____ 
    #  |__| |    |    |  | |  | |\ |  |      |__] |  | [__   |  [__      |__] |__| |__/ [__  |___ |__/ 
    #  |  | |___ |___ |__| |__| | \|  |  ___ |    |__| ___]  |  ___] ___ |    |  | |  \ ___] |___ |  \ 

    def __values_for_parser_account(self) -> Mapping:
        link = self.ui.LinkEdit.text()
        title = self.ui.title_check_box_2.isChecked()
        description = self.ui.description_check_box_2.isChecked()
        views_num = self.ui.views_num_check_box_2.isChecked()
        datetime_ = self.ui.title_check_box_2.isChecked()
        paid_goods_used = self.ui.paid_goods_used_check_box_2.isChecked()
        price = self.ui.price_check_box_2.isChecked()
        wait_time = int(self.ui.wait_spin_box.text())
        url = self.ui.url_check_box_2.isChecked()
        final_dict = ({
            "link": link,
            "title": title, 
            "description": description, 
            "views_num": views_num, 
            "datetime_": datetime_, 
            "paid_goods_used": paid_goods_used, 
            "price": price, 
            "url": url,
            "wait_time": wait_time,
            })
        return final_dict

    def __result_account_parser(self) -> None:
        final_dict = self.__values_for_parser_account()
        account_posts_parser = Account_Posts_Parser(link=final_dict["link"], parameters=final_dict)
        account_posts_parser.run()

    def __parser_account_buttons_connect(self) -> None:
        self.ui.start_scrapping_account_button.clicked.connect(self.__result_account_parser)
    
    ########################################################################################################

    ########################################################################################################
    #   ____ ____ ____ ____ ____ _  _     ___  _    ____ ____ ____     ___  ____ ____ ____ ____ ____ 
    #  [__  |___ |__| |__/ |    |__|     |__] |    |__| |    |___     |__] |__| |__/ [__  |___ |__/ 
    #  ___] |___ |  | |  \ |___ |  | ___ |    |___ |  | |___ |___ ___ |    |  | |  \ ___] |___ |  \ 

    def __search_buttons_connect(self) -> None:
        self.ui.search_place_button.clicked.connect(self.__start_searching_places)

    def __start_searching_places(self) -> None:
        search_place_parser = Search_Place_Parser(parameters=self.__values_for_parser_place())
        search_place_parser.run()

    def __values_for_parser_place(self) -> Mapping:
        wait_time = int(self.ui.wait_spin_box.text())
        final_dict = ({
            "wait_time": wait_time,
            })
        return final_dict
    

    ########################################################################################################

    ########################################################################################################
    #    ___  ____ ____ _  _ _   _     _    _ ____ ___ 
    #   |__] |__/ |  |  \/   \_/      |    | [__   |  
    #   |    |  \ |__| _/\_   |   ___ |___ | ___]  |  

    def __proxy_list_buttons_connect(self) -> None:
        self.ui.proxy_list_button.clicked.connect(self.__start_uploading_proxy_list)

    def __start_uploading_proxy_list(self) -> None:
        print("Proxy_list!")

    ########################################################################################################                       

    ########################################################################################################
    #   ___  ____ ____ ___ ____     ____ ___  _ ___ ____ ____ 
    #  |__] |  | [__   |  [__      |___ |  \ |  |  |  | |__/ 
    #  |    |__| ___]  |  ___] ___ |___ |__/ |  |  |__| |  \ 
                                                      

    def __posts_editor_buttons_connect(self) -> None:
        self.ui.posts_editor_buttonn.clicked.connect(self.__start_posts_editor)

    def __start_posts_edtior(self) -> None:
        pass

    def __values_for_posts_editor(self) -> Mapping:
        contrast = self.ui.change_contrast_check_box.text()
        direction = self.ui.change_direction_check_box.isChecked()
        text = self.ui.change_text_check_box.isChecked()
        shape_x = self.ui.shape_x_check_box.isChecked()
        size_change = self.ui.size_change_checkbox.isChecked()
        unique_pixels = self.ui.unique_pixels_checkbox.isChecked()
        x_rotate = self.ui.x_rotate_check_box.isChecked()
        final_dict = ({
            "contrast": contrast,
            "direction": direction, 
            "text": text, 
            "shape_x": shape_x, 
            "size_change": size_change, 
            "unique_pixels": unique_pixels, 
            "x_rotate": x_rotate, 
            })
        return final_dict

    ########################################################################################################                       


if __name__=="__main__":
    main_app = Main()
    main_app.show()
    sys.exit(app.exec())