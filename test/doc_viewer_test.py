from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
import os
import sys

class DocumentViewer(QWebEngineView):
    def __init__(self, parent=None):
        super(DocumentViewer, self).__init__(parent)
        
    def load_document(self, doc_path):
        # Get the absolute path of the document
        full_path = os.path.abspath(doc_path)
        # Check if the file exists
        if os.path.exists(full_path):
            # Determine the base URL, which is the directory containing the document
            base_url = QUrl.fromLocalFile(os.path.dirname(full_path) + os.sep)
            # Load the HTML content with the base URL
            with open(full_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.setHtml(html_content, baseUrl=base_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DocumentViewer()
    # Assuming 'alias.html' is in the 'docs' folder in the current directory
    viewer.load_document('docs/alias.html')
    viewer.show()
    sys.exit(app.exec_())
