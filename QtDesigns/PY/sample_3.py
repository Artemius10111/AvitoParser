# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample_3.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QStackedWidget, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 919)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 110, 1131, 711))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.gridLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Scrapping_page = QWidget()
        self.Scrapping_page.setObjectName(u"Scrapping_page")
        self.horizontalLayoutWidget = QWidget(self.Scrapping_page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1141, 651))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.AreasListWidget = QListWidget(self.horizontalLayoutWidget)
        self.AreasListWidget.setObjectName(u"AreasListWidget")

        self.verticalLayout_3.addWidget(self.AreasListWidget)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.CategoryListWidget = QListWidget(self.horizontalLayoutWidget)
        self.CategoryListWidget.setObjectName(u"CategoryListWidget")

        self.verticalLayout_3.addWidget(self.CategoryListWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.scrollArea = QScrollArea(self.horizontalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 562, 626))
        self.verticalLayoutWidget_4 = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 561, 631))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.name_only_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.name_only_check_box.setObjectName(u"name_only_check_box")

        self.verticalLayout_4.addWidget(self.name_only_check_box)

        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setMaximumSize(QSize(300, 100))

        self.verticalLayout_4.addWidget(self.label_7)

        self.title_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.title_check_box.setObjectName(u"title_check_box")

        self.verticalLayout_4.addWidget(self.title_check_box)

        self.description_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.description_check_box.setObjectName(u"description_check_box")

        self.verticalLayout_4.addWidget(self.description_check_box)

        self.views_num_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.views_num_check_box.setObjectName(u"views_num_check_box")

        self.verticalLayout_4.addWidget(self.views_num_check_box)

        self.public_date_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.public_date_check_box.setObjectName(u"public_date_check_box")

        self.verticalLayout_4.addWidget(self.public_date_check_box)

        self.paid_goods_used_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.paid_goods_used_check_box.setObjectName(u"paid_goods_used_check_box")

        self.verticalLayout_4.addWidget(self.paid_goods_used_check_box)

        self.price_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.price_check_box.setObjectName(u"price_check_box")

        self.verticalLayout_4.addWidget(self.price_check_box)

        self.url_check_box = QCheckBox(self.verticalLayoutWidget_4)
        self.url_check_box.setObjectName(u"url_check_box")

        self.verticalLayout_4.addWidget(self.url_check_box)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.depth_of_page_num_scrapping = QSpinBox(self.verticalLayoutWidget_4)
        self.depth_of_page_num_scrapping.setObjectName(u"depth_of_page_num_scrapping")

        self.horizontalLayout_4.addWidget(self.depth_of_page_num_scrapping)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget_5 = QWidget(self.Scrapping_page)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 650, 1131, 104))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ResultButton = QPushButton(self.verticalLayoutWidget_5)
        self.ResultButton.setObjectName(u"ResultButton")

        self.verticalLayout_5.addWidget(self.ResultButton)

        self.stackedWidget.addWidget(self.Scrapping_page)
        self.Scrapping_account_page = QWidget()
        self.Scrapping_account_page.setObjectName(u"Scrapping_account_page")
        self.gridLayoutWidget_2 = QWidget(self.Scrapping_account_page)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1131, 711))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setMaximumSize(QSize(300, 100))

        self.verticalLayout_7.addWidget(self.label_8)

        self.title_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.title_check_box_2.setObjectName(u"title_check_box_2")

        self.verticalLayout_7.addWidget(self.title_check_box_2)

        self.description_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.description_check_box_2.setObjectName(u"description_check_box_2")

        self.verticalLayout_7.addWidget(self.description_check_box_2)

        self.views_num_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.views_num_check_box_2.setObjectName(u"views_num_check_box_2")

        self.verticalLayout_7.addWidget(self.views_num_check_box_2)

        self.public_date_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.public_date_check_box_2.setObjectName(u"public_date_check_box_2")

        self.verticalLayout_7.addWidget(self.public_date_check_box_2)

        self.paid_goods_used_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.paid_goods_used_check_box_2.setObjectName(u"paid_goods_used_check_box_2")

        self.verticalLayout_7.addWidget(self.paid_goods_used_check_box_2)

        self.price_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.price_check_box_2.setObjectName(u"price_check_box_2")

        self.verticalLayout_7.addWidget(self.price_check_box_2)

        self.url_check_box_2 = QCheckBox(self.gridLayoutWidget_2)
        self.url_check_box_2.setObjectName(u"url_check_box_2")

        self.verticalLayout_7.addWidget(self.url_check_box_2)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.LinkEdit = QLineEdit(self.gridLayoutWidget_2)
        self.LinkEdit.setObjectName(u"LinkEdit")

        self.verticalLayout_8.addWidget(self.LinkEdit)

        self.start_scrapping_account_button = QPushButton(self.gridLayoutWidget_2)
        self.start_scrapping_account_button.setObjectName(u"start_scrapping_account_button")

        self.verticalLayout_8.addWidget(self.start_scrapping_account_button)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Scrapping_account_page)
        self.Search_place_page = QWidget()
        self.Search_place_page.setObjectName(u"Search_place_page")
        self.verticalLayoutWidget_2 = QWidget(self.Search_place_page)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 1131, 711))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.search_place_button = QPushButton(self.verticalLayoutWidget_2)
        self.search_place_button.setObjectName(u"search_place_button")

        self.verticalLayout_6.addWidget(self.search_place_button)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_6.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.Search_place_page)
        self.Proxy_list_page = QWidget()
        self.Proxy_list_page.setObjectName(u"Proxy_list_page")
        self.verticalLayoutWidget_7 = QWidget(self.Proxy_list_page)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 1131, 711))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.proxy_list_button = QPushButton(self.verticalLayoutWidget_7)
        self.proxy_list_button.setObjectName(u"proxy_list_button")

        self.verticalLayout_9.addWidget(self.proxy_list_button)

        self.textEdit_2 = QTextEdit(self.verticalLayoutWidget_7)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_9.addWidget(self.textEdit_2)

        self.stackedWidget.addWidget(self.Proxy_list_page)
        self.Image_Editor_page = QWidget()
        self.Image_Editor_page.setObjectName(u"Image_Editor_page")
        self.gridLayoutWidget_3 = QWidget(self.Image_Editor_page)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 1131, 711))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.scrollArea_2 = QScrollArea(self.gridLayoutWidget_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1125, 686))
        self.verticalLayoutWidget_8 = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 0, 1131, 631))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.verticalLayoutWidget_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        self.label_10.setMaximumSize(QSize(300, 100))

        self.verticalLayout_11.addWidget(self.label_10)

        self.change_contrast_check_box = QCheckBox(self.verticalLayoutWidget_8)
        self.change_contrast_check_box.setObjectName(u"change_contrast_check_box")

        self.verticalLayout_11.addWidget(self.change_contrast_check_box)

        self.change_text_check_box = QCheckBox(self.verticalLayoutWidget_8)
        self.change_text_check_box.setObjectName(u"change_text_check_box")

        self.verticalLayout_11.addWidget(self.change_text_check_box)

        self.unique_pixels_checkbox = QCheckBox(self.verticalLayoutWidget_8)
        self.unique_pixels_checkbox.setObjectName(u"unique_pixels_checkbox")

        self.verticalLayout_11.addWidget(self.unique_pixels_checkbox)

        self.change_direction_check_box = QCheckBox(self.verticalLayoutWidget_8)
        self.change_direction_check_box.setObjectName(u"change_direction_check_box")

        self.verticalLayout_11.addWidget(self.change_direction_check_box)

        self.x_rotate_check_box = QCheckBox(self.verticalLayoutWidget_8)
        self.x_rotate_check_box.setObjectName(u"x_rotate_check_box")

        self.verticalLayout_11.addWidget(self.x_rotate_check_box)

        self.shape_x_check_box = QCheckBox(self.verticalLayoutWidget_8)
        self.shape_x_check_box.setObjectName(u"shape_x_check_box")

        self.verticalLayout_11.addWidget(self.shape_x_check_box)

        self.size_change_checkbox = QCheckBox(self.verticalLayoutWidget_8)
        self.size_change_checkbox.setObjectName(u"size_change_checkbox")

        self.verticalLayout_11.addWidget(self.size_change_checkbox)

        self.posts_editor_button = QPushButton(self.verticalLayoutWidget_8)
        self.posts_editor_button.setObjectName(u"posts_editor_button")

        self.verticalLayout_11.addWidget(self.posts_editor_button)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea_2)


        self.gridLayout_3.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Image_Editor_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1131, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ScrappingButton = QPushButton(self.verticalLayoutWidget)
        self.ScrappingButton.setObjectName(u"ScrappingButton")

        self.horizontalLayout.addWidget(self.ScrappingButton)

        self.ScrappingAccountButton = QPushButton(self.verticalLayoutWidget)
        self.ScrappingAccountButton.setObjectName(u"ScrappingAccountButton")

        self.horizontalLayout.addWidget(self.ScrappingAccountButton)

        self.SearchPositionButton = QPushButton(self.verticalLayoutWidget)
        self.SearchPositionButton.setObjectName(u"SearchPositionButton")

        self.horizontalLayout.addWidget(self.SearchPositionButton)

        self.ProxyListButton = QPushButton(self.verticalLayoutWidget)
        self.ProxyListButton.setObjectName(u"ProxyListButton")

        self.horizontalLayout.addWidget(self.ProxyListButton)

        self.ImageEditorButton = QPushButton(self.verticalLayoutWidget)
        self.ImageEditorButton.setObjectName(u"ImageEditorButton")

        self.horizontalLayout.addWidget(self.ImageEditorButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 820, 1131, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_13.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.wait_spin_box = QSpinBox(self.horizontalLayoutWidget_2)
        self.wait_spin_box.setObjectName(u"wait_spin_box")

        self.verticalLayout_12.addWidget(self.wait_spin_box)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1130, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0433\u043e\u0440\u043e\u0434\u043e\u0432", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.name_only_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0432 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.title_check_box.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.description_check_box.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.views_num_check_box.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u043e\u0432", None))
        self.public_date_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.paid_goods_used_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u043b\u0432\u0430\u043d\u044b \u043b\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u0440\u043e\u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f", None))
        self.price_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.url_check_box.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e \u043a\u0430\u043a\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u043f\u0430\u0440\u0441\u0438\u043d\u0433 \u043a\u043e\u043d\u0442\u0435\u043d\u0442\u0430?", None))
        self.ResultButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0430\u0440\u0441\u0435\u0440", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.title_check_box_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.description_check_box_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.views_num_check_box_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u043e\u0432", None))
        self.public_date_check_box_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.paid_goods_used_check_box_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u043b\u0432\u0430\u043d\u044b \u043b\u0438 \u0443\u0441\u043b\u0443\u0433\u0438 \u043f\u0440\u043e\u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f", None))
        self.price_check_box_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.url_check_box_2.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.LinkEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.start_scrapping_account_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u043f\u0430\u0440\u0441\u0435\u0440\u0430 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.search_place_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u043c\u0435\u0441\u0442\u0430 \u0432 \u043f\u043e\u0438\u0441\u043a\u0435", None))
        self.proxy_list_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u043e\u043a\u0441\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.change_contrast_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u0442\u0440\u0430\u0441\u0442\u0430 ", None))
        self.change_text_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.unique_pixels_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043d\u0438\u043a\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0438\u043a\u0441\u0435\u043b\u0435\u0439", None))
        self.change_direction_check_box.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0437\u0435\u0440\u043a\u0430\u043b\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.x_rotate_check_box.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442 \u043d\u0430 \u0425 \u0433\u0440\u0430\u0434\u0443\u0441\u043e\u0432", None))
        self.shape_x_check_box.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u043d\u0430 \u0425 \u043f\u0438\u043a\u0441\u0435\u043b\u0435\u0439", None))
        self.size_change_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043c\u0430\u0441\u0448\u0442\u0430\u0431\u0430", None))
        self.posts_editor_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AvitoParser", None))
        self.ScrappingButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0441\u0438\u043d\u0433", None))
        self.ScrappingAccountButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0441\u0438\u043d\u0433 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.SearchPositionButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0432 \u043f\u043e\u0438\u0441\u043a\u0435", None))
        self.ProxyListButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043a\u0441\u0438 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.ImageEditorButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430", None))
    # retranslateUi

