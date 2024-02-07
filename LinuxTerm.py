from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys


class LinuxTermWidget(QWebEngineView):
    def __init__(self):
        super(LinuxTermWidget, self).__init__()
        self.setWindowTitle("Linux Terminal")

    def load_term(self):
        term_url = QUrl('https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192')
        self.load(term_url)

# Example usage
if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = LinuxTermWidget()
    widget.load_term()
    widget.show()
    sys.exit(app.exec_())