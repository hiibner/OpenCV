from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
from imgreader import analyzer
from matcheswindow import Matcheswindow
from resizer import resize, convert
import os
from mainwindow_gui import Ui_mainwindow
import sys, os


class Mainwindow(Ui_mainwindow):
    def __init__(self, input_window):
        super().__init__()
        self.input_window = input_window
        self.setupUi(input_window)

        self.input_img = None
        self.input_img_converted = None
        self.input_sift_object = None
        self.top5Objects = None

        self.progressBar.setValue(0)

        self.match1 = None
        self.match2 = None
        self.match3 = None
        self.match4 = None
        self.match5 = None

        self.input_file_name = None
        self.input_directory = None

        self.serialized_path = None

        self.knnCheckBox.setChecked(True)

        self.fileOpenBtn.clicked.connect(self.openFile)
        self.evalBtn.clicked.connect(self.startPredictions)

        self.directoryBtn.clicked.connect(self.choose_directory)
        self.serializedBtn.clicked.connect(self.choose_serialized)
        self.drawBtn.clicked.connect(self.draw_image)

    def draw_image(self):
        import drawinput
        image = cv2.imread("my_drawing.png", cv2.IMREAD_GRAYSCALE)
        image_converted = convert(image)
        self.imgDraw.setPixmap(QPixmap(image_converted))
        self.input_img = image
        self.input_img_converted = image_converted

    def choose_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        mydir = QFileDialog.getExistingDirectory()
        self.input_directory = mydir
        self.infofenster.setText(None)
        self.serialized_path = None

    def choose_serialized(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        tuple = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                            "All Files (*);;PNG (*.png);;JPEG (*.jpeg *jpg)", options=options)
        fileName = tuple[0]
        if fileName != '':
            self.serialized_path = fileName


    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        tuple = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;PNG (*.png);;JPEG (*.jpeg *jpg)", options=options)
        fileName = tuple[0]
        if fileName != '':
            self.input_file_name = os.path.split(fileName)[1]

            img1 = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)

            img_converted = convert(img1)
            self.imgDraw.setPixmap(QPixmap(img_converted))

            self.input_img = img1

            #Converted to set to a QLabel for Matcheswindow
            self.input_img_converted = convert(resize(img1 , 300))


    def startPredictions(self):
        if self.input_directory == None and self.serialized_path == None :
            self.infofenster.setText("FEHLER : Kein Monogrammverzeichnis oder PickleDatei ausgewählt")
            return
        elif self.imgDraw == None:
            self.infofenster.setText("FEHLER : Kein Eingabebild ausgewählt")
        else:
            knn = False
            skel = False
            res = False

            if self.knnCheckBox.isChecked():
                knn = True

            if self.skelCheckBox.isChecked():
                skel = True

            input_sift_object, database_objects = analyzer(self.input_img, self.input_file_name, knn, skel, res, self.input_directory, self, self.serialized_path)

            self.input_sift_object = input_sift_object
            self.top5Objects = database_objects[:5]

            self.matcheswindow = QtWidgets.QMainWindow()
            self.ui_matcheswindow = Matcheswindow(self.matcheswindow, self, skel or res)
            self.input_window.hide()
            self.matcheswindow.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    main = Mainwindow(window)
    window.show()
    sys.exit(app.exec_())