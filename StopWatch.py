import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QIcon, QFont


class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.label = QLabel("00:00:00.0",self)
        self.timer = QTimer(self)

        self.start_btn = QPushButton("Start", self)
        self.pause_btn = QPushButton("Pause", self)
        self.reset_btn = QPushButton("Reset", self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.setWindowTitle("Digital Clock")

        vbox = QVBoxLayout()

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        vbox2 = QHBoxLayout()

        vbox2.addWidget(self.start_btn)
        vbox2.addWidget(self.pause_btn)
        vbox2.addWidget(self.reset_btn)

        vbox.addLayout(vbox2)

        self.label.setAlignment(Qt.AlignCenter)

        self.label.setStyleSheet("font-size:150px;"
                                 "color: green;"
                                 )
        #self.setStyleSheet("background-color: black;")

        self.start_btn.clicked.connect(self.start)
        self.pause_btn.clicked.connect(self.pause)
        self.reset_btn.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def pause(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        second = time.second()
        millisecond = time.msec()

        return f"{hours:02}:{minutes:02}:{second:02}.{millisecond:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())

