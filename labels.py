import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabel("Hello", self)
        
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