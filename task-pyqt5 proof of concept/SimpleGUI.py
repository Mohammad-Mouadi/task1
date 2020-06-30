import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class HelloWindow(QMainWindow):
    clicked = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Hello world program")

        self.l1 = QLabel(self)
        self.l1.move(50,50)
        self.button1 = QPushButton(self)
        self.button1.setText("Click me")
        self.button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        HelloWindow.clicked += 1
        self.l1.setText("You have clicked " + str(HelloWindow.clicked) + " times")
        self.l1.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
