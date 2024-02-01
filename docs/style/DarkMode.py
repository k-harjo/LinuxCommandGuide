# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:30:23 2023

@author: e436482
"""


class DarkMode:
    
    style = """


QWidget {
    background-color: #282828;
    color: #ffffff;
    font-family: Arial;
}

QPushButton {
    background-color: #333333;
    border: 1px solid #555555;
}

QPushButton:hover {
    background-color: #555555;
}

QPushButton:pressed {
    background-color: #222222;
}

QLineEdit {
    background-color: #333333;
    border: 1px solid #555555;
}

QTextEdit {
    background-color: #333333;
    border: 1px solid #555555;
}

QListWidget {
    background-color: #333333;
    border: 1px solid #555555;
}

QListWidgetItem {
}

QListWidgetItem:selected {
    background-color: #555555;
}

QMenuBar {
    background-color: #333333;
}

QMenu {
    background-color: #333333;
}

QMenu::item:selected {
    background-color: #555555;
}

QDockWidget {
    background-color: #282828;
    titlebar-close-icon: url(close-light.png);
    titlebar-normal-icon: url(undock-light.png);
}

QStatusBar {
    background-color: #333333;
}

QScrollBar:vertical {
    border: 2px solid grey;
    background: #282828;
    width: 15px;
    margin: 22px 0 22px 0;
}

QScrollBar::handle:vertical {
    background: #555555;
}

QScrollBar::add-line:vertical {
    border: 2px solid grey;
    background: #282828;
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    border: 2px solid grey;
    background: #282828;
    height: 20px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    border: 2px solid grey;
    width: 3px;
    height: 3px;
    background: white;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QToolBar {
    border: 0px;
    background: #282828;
}
QProgressBar::chunk {
    background: #000000;

}

"""
