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
                             QListView, 
                             QComboBox
                             )

class NonEditableStringListModel(QStringListModel):
    def flags(self, index):
        return super().flags(index) & ~Qt.ItemIsEditable

class DocumentViewer(QWebEngineView):
    def __init__(self, parent=None):
        super(DocumentViewer, self).__init__(parent)

    def load_document(self, doc_path):
        if doc_path:
            if doc_path.endswith('.html'):
                document_url = QUrl.fromLocalFile(doc_path)
                self.load(document_url)

            elif doc_path.endswith('.txt'):
                with open(doc_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    html_content = f"""
                    <html>
                    <head>
                        <style>
                            body {{ margin: 0; padding: 0; font-family: Arial, sans-serif; }}
                            pre {{ white-space: pre-wrap; word-wrap: break-word; }}
                        </style>
                    </head>
                    <body>
                        <pre>{content}</pre>
                    </body>
                    </html>
                    """
                    self.setHtml(html_content)

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
        self.cmd_view = QListView()
        cmd_widget = QWidget()
        cmd_layout = QVBoxLayout()
        self.model = NonEditableStringListModel(self.cmd_view)
        self.dropdown = QComboBox()
        self.dropdown.addItems(["All Commands", "Most Used in Lab", "Bash Scripting Examples"])
        
        linux_file = "linux_commands.csv"
        self.all_linux_cmds = pd.read_csv(linux_file)

        self.most_used_cmds = ["alias", "awk", "cat", "cd", "chmod", "clear", "clrm", "column", "cp", 
                               "cut", "diff", "echo", "exit", "find", "fun", "grep", "gunzip", "gzip", 
                               "locate", "ls", "mkdir", "more", "mv", "pwd", "rm", "sdiff", "sed", 
                               "sort", "top", "touch", "uniq"]


        self.doc_viewer = DocumentViewer()
        self.doc_viewer.setHtml("<html><body>Choose a term on the left to learn more!</h1></html>")

        #set viewers to layouts
        cmd_layout.addWidget(self.dropdown)
        cmd_layout.addWidget(self.cmd_view)
        cmd_widget.setLayout(cmd_layout)

        self.main_widget_layout.addWidget(cmd_widget)
        self.main_widget_layout.addWidget(self.doc_viewer)   

        #item when clicked
        self.cmd_view.doubleClicked.connect(self.item_double_clicked)
        self.dropdown.currentIndexChanged.connect(self.add_items_to_viewer)

        '''
        ##TODO: Add bash scripting examples,
         write search algorithm, 
         add search bar, 
         clean up most used commands (probably too many),
         create new graphics or cleaup the current ones
        '''
        
    def add_items_to_viewer(self):
        self.item_list = []
        self.html_list = []

        if self.dropdown.currentText() == "All Commands":
            for item in self.all_linux_cmds["Command"]:
                self.item_list.append(item)
            for doc in self.all_linux_cmds["Html_Path"]:
                self.html_list.append(doc)

        elif self.dropdown.currentText() == "Most Used in Lab":
            for item in self.most_used_cmds:
                for index, row in self.all_linux_cmds.iterrows():
                    if item == row["Command"]:
                        self.item_list.append(item)
                        self.html_list.append(row["Html_Path"])

        self.model.setStringList(self.item_list)
        self.cmd_view.setModel(self.model)

    def item_double_clicked(self, index):
        for doc in self.all_linux_cmds["Html_Path"]:
            self.html_list.append(doc)
        self.doc_viewer.setHtml("<html><body>Loading file...</h1></html>")
        doc = self.html_list[index.row()]
        self.doc_viewer.load_document(doc)  

    def new_instance(self):
        subprocess.Popen([sys.executable, __file__])

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    GUI = LinuxDictGUI()
    GUI.show()
    sys.exit(app.exec_())   