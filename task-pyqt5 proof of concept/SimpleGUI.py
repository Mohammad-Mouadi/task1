import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout
from PyQt5 import sip, QtCore, QtGui


class HelloWindow(QMainWindow):
    clicked = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Hello world program")

        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.label = QLabel(self)
        self.grid.addWidget(self.label, 1, 0)
        self.label.move(50, 50)
        self.button1 = QPushButton(self)
        self.button1.setText("Click me")
        self.button1.clicked.connect(self.button1_clicked)
        self.grid.addWidget(self.button1, 5, 0)

    def button1_clicked(self):
        HelloWindow.clicked += 1
        self.label.setText("You have clicked " + str(HelloWindow.clicked) + " times")
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    app.exec_()
