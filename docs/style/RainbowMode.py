# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:30:23 2023

@author: e436482
"""

    # background-color: qlineargradient(x1: 0, x2: 1, stop: 0 red, stop: 0.2 orange, stop: 0.4 yellow, stop: 0.6 green, stop: 0.8 blue, stop: 1 purple);
    # background-color: qconicalgradient(cx:0.5, cy:0.5, angle:30, stop: 0 red, stop: 0.2 orange, stop: 0.4 yellow, stop: 0.6 green, stop: 0.8 blue, stop: 1 purple);
    # background-color: qradialgradient(cx:0, cy:0, radius: 1, fx:0.5, fy:0.5, stop: 0 red, stop: 0.2 orange, stop: 0.4 yellow, stop: 0.6 green, stop: 0.8 blue, stop: 1 purple);


class RainbowMode:
    
    style = """


QWidget {
    background-color: qlineargradient(x1: 0, x2: 1, stop: 0 #ffccff, stop: 0.2 #ffcccc, stop: 0.4 #ffffcc , stop: 0.6 #ccffcc , stop: 0.8 #ccffff , stop: 1 #ccccff);
    color: #660066;
    font-family: Arial;
}

QPushButton {
     background-color: transparent;


    border: 1px solid #f0c1d0;
}

QPushButton:hover {
    background-color: #ffccff;
}

QPushButton:pressed {
    background-color: #ccccff;
}

QLineEdit {
    background-color: transparent;
    border: 1px solid #f0c1d0;
}

QLabel {
    background-color: transparent;
}

QTextEdit {
     background-color: transparent;


    border: 1px solid #f0c1d0;
}

QListWidget {
     background-color: transparent;


    border: 1px solid #f0c1d0;
}


QListWidgetItem:selected {
    background-color: #f0c1d0;
}

QMenuBar {
     background-color: transparent;


}

QMenu {
     background-color: #ccccff;

}

QMenu::item:selected {
    background-color: #ffccff;
}

QDockWidget {
    background-color: #ffccff;
    titlebar-normal-icon: url(undock-light.png);
}

QStatusBar {
    background-color: #ffccff;
}

QScrollBar:vertical {
    background: #f0c1d0;

}

QScrollBar::handle:vertical {
    background: #ffccff;
}

QScrollBar::add-line:vertical {
    background: #ffccff;

}

QScrollBar::sub-line:vertical {
    background: #ffccff;

}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    background: none;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QToolBar {
    border: 0px;
    background: transparent;
}

QProgressBar::chunk {
    background: #ccccff;

}

"""
