import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class HelloWindow(QMainWindow):
    clicked = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Hello world program")

        self.label = QLabel(self)
        self.label.move(50, 50)
        self.button1 = QPushButton(self)
        self.button1.setText("Click me")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        HelloWindow.clicked += 1
        self.label.setText("You have clicked " + str(HelloWindow.clicked) + " times")
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    app.exec_()
