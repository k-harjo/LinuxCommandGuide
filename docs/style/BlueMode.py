# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:30:23 2023

@author: e436482
"""


class BlueMode:
    
    style = """


QWidget {
    background-color: #DBE5FF;
    color: #091534;
    font-family: Arial;
}

QPushButton {
    background-color: #4666BE;
    color: white;
    border: 1px solid #091534;
}

QPushButton:hover {
    background-color: #88A3EC;
}

QPushButton:pressed {
    background-color: #DBE5FF;
    color: black;
}

QLineEdit {
    background-color: #DBE5FF;
    border: 1px solid #091534;
}

QTextEdit {
    background-color: #DBE5FF;
    border: 1px solid #091534;
}

QListWidget {
    background-color: #DBE5FF;
    border: 1px solid #091534;
}

QListWidgetItem {
}

QListWidgetItem:selected {
    background-color: #88A3EC;
}

QMenuBar {
    background-color: #1F377A;
    color: white;
}

QMenu {
    background-color: #4666BE;
    color: white;
}

QMenu::item:selected {
    background-color: #88A3EC;
}

QDockWidget {
    background-color: #88A3EC;
    titlebar-close-icon: url(close-light.png);
    titlebar-normal-icon: url(undock-light.png);
}

QStatusBar {
    background-color: #88A3EC;
}

QScrollBar:vertical {
    background: #4666BE;

}

QScrollBar::handle:vertical {
    background: #88A3EC;
}

QScrollBar::add-line:vertical {
    background: #4666BE;
}

QScrollBar::sub-line:vertical {
    background: #4666BE;

}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    background: none;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QToolBar {
    border: 0px;
    background: #0247FE;
}

QProgressBar::chunk {
    background: #4666BE;

}

QProgressBar {
    color: white

    }                                
                                
"""
