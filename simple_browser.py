import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView


class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Simple Web Browser")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL and press Enter")
        self.address_bar.returnPressed.connect(self.load_url)
        
        self.browser = QWebEngineView()
            
        self.layout.addWidget(self.address_bar)
        self.layout.addWidget(self.browser)
       
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.address_bar.setText("https://www.google.com")
    
    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())
