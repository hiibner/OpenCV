from detailedwindow_gui import Ui_detailedwindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os


class Detailedwindow(Ui_detailedwindow):
    def __init__(self, input_window, matcheswindow_object, int):
        super().__init__()
        self.input_window = input_window
        self.setupUi(input_window)



        self.matchimg = matcheswindow_object.matchresults[int]
        self.matcheswindow_object = matcheswindow_object

        self.label.setPixmap(QPixmap(self.matchimg))
        self.backBtn.clicked.connect(self.backtomatches)

    def backtomatches(self):
        self.input_window.close()
        self.matcheswindow_object.input_window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    main = Detailedwindow(window)
    window.show()
    sys.exit(app.exec_())
