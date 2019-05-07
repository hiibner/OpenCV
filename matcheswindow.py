from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resizer import resize, convert, rgb2qimage
from detailedwindow import Detailedwindow
import cv2
from matcheswindow_gui import Ui_matcheswindow
import sys, os

class Matcheswindow(Ui_matcheswindow):
    def __init__(self, input_window, mainwindow_object, modified=False):
        super().__init__()
        self.input_window = input_window
        self.setupUi(input_window)



        self.mainwindow_object = mainwindow_object
        self.input_pic = mainwindow_object.input_img_converted


        #Original Bilder die zum Input gematched wurden
        self.match1 = convert(resize(self.mainwindow_object.top5Objects[0].imgdata, 150))
        self.match2 = convert(resize(self.mainwindow_object.top5Objects[1].imgdata, 150))
        self.match3 = convert(resize(self.mainwindow_object.top5Objects[2].imgdata, 150))
        self.match4 = convert(resize(self.mainwindow_object.top5Objects[3].imgdata, 150))
        self.match5 = convert(resize(self.mainwindow_object.top5Objects[4].imgdata, 150))

        #Modifizierte Bilder die zum Input gematched wurden

        self.match1_modified = convert(resize(self.mainwindow_object.top5Objects[0].img_data_skeleton, 150))
        self.match2_modified = convert(resize(self.mainwindow_object.top5Objects[1].img_data_skeleton, 150))
        self.match3_modified = convert(resize(self.mainwindow_object.top5Objects[2].img_data_skeleton, 150))
        self.match4_modified = convert(resize(self.mainwindow_object.top5Objects[3].img_data_skeleton, 150))
        self.match5_modified = convert(resize(self.mainwindow_object.top5Objects[4].img_data_skeleton, 150))


        #Matching Ergebnisse der Einzelnen Matches
        self.match1Result = rgb2qimage(cv2.resize(self.mainwindow_object.top5Objects[0].matching_result,(360,300)))
        self.match2Result = rgb2qimage(cv2.resize(self.mainwindow_object.top5Objects[1].matching_result,(360,300)))
        self.match3Result = rgb2qimage(cv2.resize(self.mainwindow_object.top5Objects[2].matching_result,(360,300)))
        self.match4Result = rgb2qimage(cv2.resize(self.mainwindow_object.top5Objects[3].matching_result,(360,300)))
        self.match5Result = rgb2qimage(cv2.resize(self.mainwindow_object.top5Objects[4].matching_result,(360,300)))

        self.matchresults = [self.match1Result, self.match2Result, self.match3Result, self.match4Result,
                             self.match5Result]





        # Ab hier Events

        # Vorschaubilder
        self.m1.setPixmap(QPixmap(self.match1))
        self.m2.setPixmap(QPixmap(self.match2))
        self.m3.setPixmap(QPixmap(self.match3))
        self.m4.setPixmap(QPixmap(self.match4))
        self.m5.setPixmap(QPixmap(self.match5))

        self.inputIMG.setPixmap(QPixmap(self.input_pic))

        if modified == True:
            # Vorschau der modifizierten Bilder
            self.modified_label.setText("Modifiziertes Bild")
            self.original_label.setText("Original Bild")
            self.skel1.setPixmap(QPixmap(self.match1_modified))
            self.skel2.setPixmap(QPixmap(self.match2_modified))
            self.skel3.setPixmap(QPixmap(self.match3_modified))
            self.skel4.setPixmap(QPixmap(self.match4_modified))
            self.skel5.setPixmap(QPixmap(self.match5_modified))

            self.skel_input.setPixmap(QPixmap(convert(resize(self.mainwindow_object.input_sift_object.img_data_skeleton, 300))))


        # VorschauNamen
        self.match1Name.setText(self.mainwindow_object.top5Objects[0].imgname)
        self.match2Name.setText(self.mainwindow_object.top5Objects[1].imgname)
        self.match3Name.setText(self.mainwindow_object.top5Objects[2].imgname)
        self.match4Name.setText(self.mainwindow_object.top5Objects[3].imgname)
        self.match5Name.setText(self.mainwindow_object.top5Objects[4].imgname)

        self.inputImgName.setText(self.mainwindow_object.input_file_name)

        # Buttons
        self.match1Btn.clicked.connect(self.showMatch1)
        self.match2Btn.clicked.connect(self.showMatch2)
        self.match3Btn.clicked.connect(self.showMatch3)
        self.match4Btn.clicked.connect(self.showMatch4)
        self.match5Btn.clicked.connect(self.showMatch5)

        self.backBtn.clicked.connect(self.closeSecond)


    def closeSecond(self):
        self.mainwindow_object.progressBar.setValue(0)
        self.input_window.close()
        self.mainwindow_object.input_window.show()


    def showMatch1(self):
        self.detailedwindow = QtWidgets.QMainWindow()
        self.ui_detailedwindow = Detailedwindow(self.detailedwindow, self, 0)
        self.input_window.hide()
        self.detailedwindow.show()

    def showMatch2(self):
        self.detailedwindow = QtWidgets.QMainWindow()
        self.ui_detailedwindow = Detailedwindow(self.detailedwindow, self, 1)
        self.input_window.hide()
        self.detailedwindow.show()

    def showMatch3(self):
        self.detailedwindow = QtWidgets.QMainWindow()
        self.ui_detailedwindow = Detailedwindow(self.detailedwindow, self, 2)
        self.input_window.hide()
        self.detailedwindow.show()

    def showMatch4(self):
        self.detailedwindow = QtWidgets.QMainWindow()
        self.ui_detailedwindow = Detailedwindow(self.detailedwindow, self, 3)
        self.input_window.hide()
        self.detailedwindow.show()

    def showMatch5(self):
        self.detailedwindow = QtWidgets.QMainWindow()
        self.ui_detailedwindow = Detailedwindow(self.detailedwindow, self, 4)
        self.input_window.hide()
        self.detailedwindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    main = Matcheswindow(window)
    window.show()
    sys.exit(app.exec_())
