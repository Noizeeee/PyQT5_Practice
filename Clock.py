import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QIcon, QFont


class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.timer = QTimer(self)

        self.start = QPushButton("Start", self)
        self.pause = QPushButton("Pause", self)
        self.reset = QPushButton("Reset", self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.setWindowTitle("Digital Clock")

        vbox = QVBoxLayout()

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        vbox2 = QHBoxLayout()

        vbox2.addWidget(self.start)
        vbox2.addWidget(self.pause)
        vbox2.addWidget(self.reset)

        vbox.addLayout(vbox2)

        self.label.setAlignment(Qt.AlignCenter)

        self.label.setStyleSheet("font-size:150px;"
                                 "color: green;"
                                 )
        #self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())

