import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel("Hello", self)
        label.setFont(QFont("Times New Roman", 20))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: red;" "background-color: blue;")

        #label.setAlignment(Qt.AlignTop) #ALign top Vertically
        #label.setAlignment(Qt.AlignBottom) #ALign bottom Vertically
        #label.setAlignment(Qt.AlignVCenter) #ALign Center Vertically

        #label.setAlignment(Qt.AlignRight) #ALign Right Horizontally
        #label.setAlignment(Qt.AlignLeft) #ALign Left Horizontally
        #label.setAlignment(Qt.AlignHCenter) #ALign Center Horizontally

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #ALign Center and Top

        self.setWindowIcon(QIcon('ID.jpg'))
        self.setWindowTitle("Random Label")
        self.setGeometry(700, 400, 500, 500)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()