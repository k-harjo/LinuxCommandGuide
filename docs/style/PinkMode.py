# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:30:23 2023

@author: e436482
"""


class PinkMode:
    
    style = """


QWidget {
    background-color: #f0c1d0;
    color: #7b1e3b;
    font-family: Arial;
}

QPushButton {
    background-color: #faeaef;
    border: 1px solid #f0c1d0;
}

QPushButton:hover {
    background-color: #f0c1d0;
}

QPushButton:pressed {
    background-color: #222222;
}

QLineEdit {
    background-color: #faeaef;
    border: 1px solid #f0c1d0;
    padding: 5px;
}

QTextEdit {
    background-color: #faeaef;
    border: 1px solid #f0c1d0;
}

QListWidget {
    background-color: #faeaef;
    border: 1px solid #f0c1d0;
}

QListWidgetItem {
}

QListWidgetItem:selected {
    background-color: #f0c1d0;
}

QMenuBar {
    background-color: #faeaef;
}

QMenu {
    background-color: #faeaef;
}

QMenu::item:selected {
    background-color: #f0c1d0;
}

QDockWidget {
    background-color: #faeaef;
    titlebar-close-icon: url(close-light.png);
    titlebar-normal-icon: url(undock-light.png);
}

QStatusBar {
    background-color: #faeaef;
}

QScrollBar:vertical {
    border: 2px solid grey;
    background: #f0c1d0;
    width: 15px;
    margin: 22px 0 22px 0;
}

QScrollBar::handle:vertical {
    background: #f0c1d0;
    min-height: 20px;
}

QScrollBar::add-line:vertical {
    border: 2px solid grey;
    background: #f0c1d0;
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    border: 2px solid grey;
    background: #f0c1d0;
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
    background: #f0c1d0;
}

"""
