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
        self.label1.setStyleSheet("color: red;" "background-color: red;")
        self.label2.setStyleSheet("color: red;" "background-color: orange;")
        self.label3.setStyleSheet("color: red;" "background-color: yellow;")
        self.label4.setStyleSheet("color: red;" "background-color: green;")
        self.label5.setStyleSheet("color: red;" "background-color: blue;")
        central_widget = QWidget()
        vbox = QHBoxLayout()

        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.label5)

        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()