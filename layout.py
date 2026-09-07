import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel("1",self)
        self.label2 = QLabel("2",self)
        self.label3 = QLabel("3",self)
        self.label4 = QLabel("4",self)
        self.label5 = QLabel("5",self)

        self.initUI()
        

    def initUI(self):
        central_widget = QWidget()
        self.label1.setFont(QFont("Times New Roman", 20))
        self.label1.setGeometry(0, 0, 500, 100)
        self.label1.setStyleSheet("color: red;" "background-color: blue;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()