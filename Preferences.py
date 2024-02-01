import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QApplication, QPushButton
from PyQt5.QtCore import pyqtSignal
from docs.style.StandardStyle import StandardStyle
from docs.style.BlueMode import BlueMode
from docs.style.DarkMode import DarkMode
from docs.style.PinkMode import PinkMode
from docs.style.RainbowMode import RainbowMode

class Preferences(QWidget):
    mode_changed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.pref_window = QWidget()
        self.layout = QVBoxLayout()
        self.setWindowTitle('Preferences')
        self.setFixedSize(500, 300)
        self.setLayout(self.layout)

        # Create radio buttons
        self.standard_mode_radio = QRadioButton("Default Mode")
        self.blue_mode_radio = QRadioButton("Blue Mode")
        self.dark_mode_radio = QRadioButton("Dark Mode")
        self.pink_mode_radio = QRadioButton("Pink Mode")
        self.rainbow_mode_radio = QRadioButton("Rainbow Mode")

        # Create layout and add radio buttons
        self.layout.addWidget(self.standard_mode_radio)
        self.layout.addWidget(self.blue_mode_radio)
        self.layout.addWidget(self.dark_mode_radio)
        self.layout.addWidget(self.pink_mode_radio)
        self.layout.addWidget(self.rainbow_mode_radio)
        
        #create apply button
        self.apply_button = QPushButton('Apply')
        self.layout.addWidget(self.apply_button)
        self.apply_button.clicked.connect(self.apply_preferences)

    def apply_preferences(self):
        selected_mode = ''
        if self.standard_mode_radio.isChecked():
            selected_mode = StandardStyle.style
        elif self.blue_mode_radio.isChecked():
            selected_mode = BlueMode.style
        elif self.dark_mode_radio.isChecked():
            selected_mode = DarkMode.style
        elif self.pink_mode_radio.isChecked():
            selected_mode = PinkMode.style
        elif self.rainbow_mode_radio.isChecked():
            selected_mode = RainbowMode.style
        self.mode_changed.emit(selected_mode)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    preferences = Preferences()
    preferences.show()
    sys.exit(app.exec_())
