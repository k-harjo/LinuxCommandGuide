'''
Created on Tue Oct 10 09:10:32 2023

@author: e436482


'''


import os
from functools import partial
from pathlib import Path
# import argparse
# import threading
# import random
# import time
import datetime
import csv
import sys
import subprocess
import time
import pandas as pd
from PyQt5.QtCore import (QTimerEvent, 
                          QStringListModel, 
                          Qt, 
                          QThread, 
                          QMutex,
                          QObject, 
                          pyqtSignal, 
                          QUrl, 
                          QThreadPool, 
                          QProcess, 
                          QTimer
                        )
from PyQt5.QtGui import (QKeySequence, 
                         QDesktopServices, 
                         QIcon, 
                         QFont                         
                         )
from PyQt5.QtWidgets import (QMainWindow,
                             QDockWidget, 
                             QWidget, 
                             QLabel, 
                             QPushButton, 
                             QComboBox, 
                             QLineEdit,
                             QApplication, 
                             QHBoxLayout, 
                             QVBoxLayout, 
                             QToolBar, 
                             QAction,
                             QFileSystemModel,
                             QTextBrowser, 
                             QFileDialog, 
                             QMessageBox, 
                             QDialog, 
                             QProgressBar, 
                             QProgressDialog, 
                             QTextEdit, 
                             QRadioButton,
                             QGroupBox, 
                             QScrollBar, 
                             QScrollArea
                             
                             )

class LinuxDictGUI(QMainWindow):
    """
    """
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(1200, 900)
        self.setWindowTitle("Linux and Bash Helper")
        self.setWindowIcon(QIcon(''))

        self.main_widget = QWidget()
        self.main_widget_layout = QHBoxLayout()

        self.setCentralWidget(self.main_widget)

        self.main_widget.setLayout(self.main_widget_layout)


        '''
        Main Window Menus 
        '''
        self.menubar = self.menuBar()
        
        #file menu
        file_menu =self.menubar.addMenu("File")
        new = QAction("New", self)
        file_menu.addAction(new)
        new.setShortcut(QKeySequence.Quit)
        new.triggered.connect(self.new_instance)               
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)               
        file_menu.addAction(exit_action)   
                
        #settings menu
        settings_menu = self.menubar.addMenu("Settings")
        preferences = QAction("Preferences", self)
        # preferences.triggered.connect(self.show_preferences)
        settings_menu.addAction(preferences)
        
        #help menu
        help_menu = self.menubar.addMenu("Help")
        
        user_manual = QAction("User Manual", self)
        # user_manual.triggered.connect(self.open_user_manual)
        help_menu.addAction(user_manual)

        about = QAction("About", self)
        # about.triggered.connect(self.open_about)
        help_menu.addAction(about)
        
        an_steps = QAction("Analysis Steps", self)
        # an_steps.triggered.connect(self.open_analysis_steps)
        help_menu.addAction(an_steps)


        '''
        Widgets
        '''
        cmd_widget = QWidget()
        list_layout=QVBoxLayout()

        file = "linux_commands.csv"
        all_linux_cmds = pd.read_csv(file)
        button_list = []
        for item in all_linux_cmds["Command"]:
            button = QPushButton()
            button.setText(item)
            button_list.append(button)

        for index, item in enumerate(button_list):
            list_layout.addWidget(button_list[index])

        cmd_widget.setLayout(list_layout)
        self.main_widget_layout.addWidget(cmd_widget)     


        # self.show_stuff_widget = QWidget()
        # viewer_layout = QVBoxLayout()

        # self.linux_doc = "Linux_Command_guide.pdf"
        # viewer_layout.addItem(self.linux_doc)

        # self.show_stuff_widget.setLayout(viewer_layout)

        # self.main_widget_layout.addWidget(self.show_stuff_widget)


    def new_instance(self):
        subprocess.Popen([sys.executable, __file__])

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    GUI = LinuxDictGUI()
    GUI.show()
    sys.exit(app.exec_())   