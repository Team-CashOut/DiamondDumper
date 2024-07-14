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
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, pyqtSlot, QThread, QThreadPool, QBasicTimer, QTimerEvent, QMessageLogContext, QtMsgType, QRect
from PyQt5.QtWidgets import QApplication, QScrollArea, QLineEdit, QHBoxLayout, QShortcut, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar, QTableWidgetItem
import sqlite3
import telebot
import subprocess
import telebot
from telebot import TeleBot

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the UI file
        uic.loadUi('dumper.ui', self)

        self.dumpDocument_button.clicked.connect(self.sendDocument_function)
        self.dumpMessage_button.clicked.connect(self.dumpMessages)
        self.start_button.clicked.connect(self.start_function)
        self.stop_button.clicked.connect(self.stop_function)
        self.dumpPhoto_button.clicked.connect(self.dumpPhoto_function)
        self.submit_single_token_button.clicked.connect(self.checkTelegramBotStatus)
        self.console_text_response_button.clicked.connect(self.handleUserResponse)
        self.load_database_button.clicked.connect(self.openDatabaseFileDialog)
        self.import_bulk_button.clicked.connect(self.importBulkTokens)

        # Define the tableWidget columns
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels([
            "No.", "Token", "Bot Name", "Username", "Status",
            "Submission Date", "Last Checked Date", "Last Dumped Date"
        ])

        # Load existing bots from the database
        self.loadBotsFromDatabase()
        self.displayStatsAndCounts()
        self.sync_button.clicked.connect(self.launch_bot)
        self.botManager_button.clicked.connect(self.launch_bot)




    def sendMessage_function(self):
        pass
    
    def sendDocument_function(self):
        pass

    def start_function(self):
        pass

    def stop_function(self):
        pass

    def dumpPhoto_function(self):
        pass

    def checkTelegramBotStatus(self):
        token = self.single_token_submittion_text_input.toPlainText()
        url = f'https://api.telegram.org/bot{token}/getMe'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if the response status code indicates an error

            if response.status_code == 200:
                self.console_text_edit.append("Telegram Bot is online!")
                json_data = json.loads(response.content)
                self.displayJSON(json_data)
                self.console_text_edit.append("Do you want to save this bot to your database? (Y/N)")

        except requests.exceptions.RequestException as e:
            error_msg = f"An error occurred during the request:\n{str(e)}"
            QMessageBox.critical(self, "Error", error_msg)

    def displayJSON(self, json_data):
        # Convert the JSON data to a formatted string for display
        formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
        self.console_text_edit.append(formatted_json)

    def handleUserResponse(self):
        user_response = self.console_text_response_input.toPlainText()
        self.console_text_edit.append(f"Hackers response: {user_response}")

        if user_response.upper() == 'Y':
            # Add bot to the database
            self.addToDatabase()

    def importBulkTokens(self):
        # Get the file path from the import_bulk_file_path_text_edit
        file_path = self.import_bulk_file_path_text_edit.toPlainText()

        try:
            with open(file_path, 'r') as file:
                # Read the contents of the file line by line
                lines = file.readlines()

                # Process each line as a separate token and display the response in the console
                for line in lines:
                    token = line.strip()
                    self.console_text_edit.append(f"Processing token: {token}")
                    self.checkTelegramBotStatus(token)
                    self.addToDatabase(token)

        except FileNotFoundError:
            self.console_text_edit.append(f"File not found: {file_path}")
        except OSError:
            self.console_text_edit.append(f"Error reading file: {file_path}")

    def addToDatabase(self, token):
        # Get the bot details from the token
        bot_name = "My Bot"  # Replace this with the actual bot name
        username = "mybotusername"  # Replace this with the actual bot username
        status = "Online"  # Replace this with the actual bot status
        submission_date = datetime.date.today().strftime('%Y-%m-%d')  # Get the current date as the submission date
        last_checked_date = ""  # Replace this with the actual last checked date
        last_dumped_date = ""  # Replace this with the actual last dumped date

        # Connect to the database
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        # Insert the bot details into the database
        cursor.execute("INSERT INTO bots (token, bot_name, username, status, submission_date, last_checked_date, last_dumped_date) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (token, bot_name, username, status, submission_date, last_checked_date, last_dumped_date))

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Refresh the tableWidget to show the updated data
        self.loadBotsFromDatabase()

    def checkTelegramBotStatus(self, token):
        # Update the code of the checkTelegramBotStatus function to accept the token argument
        url = f'https://api.telegram.org/bot{token}/getMe'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if the response status code indicates an error

            if response.status_code == 200:
                self.console_text_edit.append("Telegram Bot is online!")
                json_data = json.loads(response.content)
                self.displayJSON(json_data)
                self.console_text_edit.append("Do you want to save this bot to your database? (Y/N)")

        except requests.exceptions.RequestException as e:
            error_msg = f"An error occurred during the request:\n{str(e)}"
            QMessageBox.critical(self, "Error", error_msg)





    def addToDatabase(self):
        # Get the bot details from the JSON response or user input
        token = self.single_token_submittion_text_input.toPlainText()
        bot_name = "My Bot"  # Replace this with the actual bot name from the JSON response or user input
        username = "mybotusername"  # Replace this with the actual bot username from the JSON response or user input
        status = "Online"  # Replace this with the actual status from the JSON response or user input
        submission_date = datetime.date.today().strftime('%Y-%m-%d')  # Get the current date as the submission date
        last_checked_date = ""  # Replace this with the actual last checked date
        last_dumped_date = ""  # Replace this with the actual last dumped date
        
        # Get the current row count in the tableWidget
        row_count = self.tableWidget.rowCount()
        
        # Insert a new row at the bottom
        self.tableWidget.insertRow(row_count)
        
        # Set the values for each column
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem(token))
        self.tableWidget.setItem(row_count, 2, QTableWidgetItem(bot_name))
        self.tableWidget.setItem(row_count, 3, QTableWidgetItem(username))
        self.tableWidget.setItem(row_count, 4, QTableWidgetItem(status))
        self.tableWidget.setItem(row_count, 5, QTableWidgetItem(submission_date))
        self.tableWidget.setItem(row_count, 6, QTableWidgetItem(last_checked_date))
        self.tableWidget.setItem(row_count, 7, QTableWidgetItem(last_dumped_date))
        self.loadBotsFromDatabase()

    def loadBotsFromDatabase(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS bots (token TEXT, bot_name TEXT, username TEXT, status TEXT, submission_date TEXT, last_checked_date TEXT, last_dumped_date TEXT)")
        cursor.execute("SELECT * FROM bots")
        bot_records = cursor.fetchall()

        for i, bot in enumerate(bot_records):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(bot[0]))  # Assuming token is in the first column
            self.tableWidget.setItem(i, 2, QTableWidgetItem(bot[1]))  # Assuming bot name is in the second column
            self.tableWidget.setItem(i, 3, QTableWidgetItem(bot[2]))  # Assuming username is in the third column
            self.tableWidget.setItem(i, 4, QTableWidgetItem(bot[3]))  # Assuming status is in the fourth column
            self.tableWidget.setItem(i, 5, QTableWidgetItem(bot[4]))  # Assuming submission date is in the fifth column
            self.tableWidget.setItem(i, 6, QTableWidgetItem(bot[5]))  # Assuming last checked date is in the sixth column
            self.tableWidget.setItem(i, 7, QTableWidgetItem(bot[6]))  # Assuming last dumped date is in the seventh column

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
            self.tableWidget.setItem(i, 1, QTableWidgetItem(bot[0]))  # Token
            self.tableWidget.setItem(i, 2, QTableWidgetItem(bot[1]))  # Bot Name
            self.tableWidget.setItem(i, 3, QTableWidgetItem(bot[2]))  # Username
            self.tableWidget.setItem(i, 4, QTableWidgetItem(bot[3]))  # Status
            self.tableWidget.setItem(i, 5, QTableWidgetItem(bot[4]))  # Submission Date
            self.tableWidget.setItem(i, 6, QTableWidgetItem(bot[5]))  # Last Checked Date
            self.tableWidget.setItem(i, 7, QTableWidgetItem(bot[6]))  # Last Dumped Date
    
        cursor.close()
        connection.close()


    
    def displayStatsAndCounts(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
    
        # Count the total number of bots in the database
        cursor.execute("SELECT COUNT(*) FROM bots")
        total_bots_count = cursor.fetchone()[0]
    
        # Count the number of online bots in the database
        cursor.execute("SELECT COUNT(*) FROM bots WHERE status = 'Online'")
        online_bots_count = cursor.fetchone()[0]
    
        # Count the number of offline bots in the database
        cursor.execute("SELECT COUNT(*) FROM bots WHERE status = 'Offline'")
        offline_bots_count = cursor.fetchone()[0]
    
        # Count the number of bots with the last checked date as today
        today_date = datetime.date.today().strftime('%Y-%m-%d')
        cursor.execute("SELECT COUNT(*) FROM bots WHERE last_checked_date = ?", (today_date,))
        today_checked_bots_count = cursor.fetchone()[0]
    
        # Count the number of bots with the last dumped date as today
        cursor.execute("SELECT COUNT(*) FROM bots WHERE last_dumped_date = ?", (today_date,))
        today_dumped_bots_count = cursor.fetchone()[0]
    
        # Display the stats and counts in the sub_console_frame_text
        stats_text = f"Total Bots count: {total_bots_count}\n"
        stats_text += f"Online Bots count: {online_bots_count}\n"
        stats_text += f"Offline Bots count: {offline_bots_count}\n"
        stats_text += f"Bots Checked today: {today_checked_bots_count}\n"
        stats_text += f"Bots Dumped today: {today_dumped_bots_count}\n"
    
        self.sub_console_frame_text.append(stats_text)
    
        cursor.close()
        connection.close()





    def dumpMessages(self):
        # Check if any row is selected in the table widget
        selected_rows = self.tableWidget.selectedItems()
        if len(selected_rows) == 0:
            self.displayErrorMessage("No bot selected. Please select a bot from the table.")
            return
    
        # Get the bot details from the selected row
        bot_token = selected_rows[1].text()
        bot_name = selected_rows[2].text()
    
        # Display a confirmation message dialog
        confirm_dialog = QtWidgets.QMessageBox()
        confirm_dialog.setIcon(QtWidgets.QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirm Dump")
        confirm_dialog.setText(f"Do you want to dump all messages from bot '{bot_name}'?")
        confirm_dialog.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirm_dialog.setDefaultButton(QtWidgets.QMessageBox.No)
    
        # Check the user's response
        response = confirm_dialog.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            # User confirmed, proceed with dumping messages
            try:
                # Make a request to dump messages from the bot using the token
                dump_url = f"https://api.telegram.org/bot{bot_token}/dumpMessages"
                response = requests.get(dump_url)
    
                if response.status_code == 200:
                    # Successfully dumped messages
                    self.displaySuccessMessage("Messages dumped successfully.")
                else:
                    # Failed to dump messages
                    self.displayErrorMessage("Failed to dump messages. Please try again.")
                
            except requests.exceptions.RequestException as e:
                # Exception occurred during the request
                self.displayErrorMessage(f"An error occurred during the request: {str(e)}")
        
        else:
            # User canceled, do nothing
            return
















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())