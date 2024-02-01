'''
Created on Tue Oct 10 09:10:32 2023

@author: e436482


'''


import os
from functools import partial
from pathlib import Path
import datetime
import csv
import sys
import subprocess
import time
import pandas as pd
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import (QTimerEvent, 
                          QStringListModel, 
                          Qt,
                          QUrl
                        )
from PyQt5.QtGui import (QKeySequence, 
                         QIcon
                         )
from PyQt5.QtWidgets import (QMainWindow,                        
                             QWidget, 
                             QApplication,
                             QGridLayout, 
                             QHBoxLayout, 
                             QVBoxLayout,  
                             QAction,
                             QListView
                             )

class NonEditableStringListModel(QStringListModel):
    def flags(self, index):
        return super().flags(index) & ~Qt.ItemIsEditable

class LinuxDictGUI(QMainWindow):
    """
    """
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(1200, 900)
        self.setWindowTitle("Linux and Bash Helper")
        self.setWindowIcon(QIcon(''))

        self.main_widget = QWidget()
        self.main_widget_layout = QGridLayout()

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
        self.cmd_view = QListView()
        self.model = NonEditableStringListModel(self.cmd_view)

        file = "linux_commands.csv"
        all_linux_cmds = pd.read_csv(file)

        self.item_list = []
        for item in all_linux_cmds["Command"]:
            self.item_list.append(item)
        self.model.setStringList(self.item_list)
        self.cmd_view.setModel(self.model)

        self.doc_viewer = QWebEngineView()
        self.docs_list = []
        for doc in all_linux_cmds["Doc_Path"]:
            self.docs_list.append(doc)
        print(self.docs_list)

        self.doc_viewer.setHtml("<html><body><h1>Hello World</h1></body></html>")

        #item when clicked
        self.cmd_view.doubleClicked.connect(self.item_double_clicked)

        #set viewers to layout
        self.main_widget_layout.addWidget(self.doc_viewer, 0, 1)     
        self.main_widget_layout.addWidget(self.cmd_view, 0, 0)

    def item_double_clicked(self, index):
        doc = self.docs_list[index.row()]
        print(doc)  
        if doc:  
            document_url = QUrl.fromLocalFile(doc)
            # self.doc_viewer.setUrl(document_url)
            self.doc_viewer.load(document_url)  

    def new_instance(self):
        subprocess.Popen([sys.executable, __file__])

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    GUI = LinuxDictGUI()
    GUI.show()
    sys.exit(app.exec_())   