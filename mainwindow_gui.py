# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hyu\PycharmProjects\OpenCV\uis\mainwindow_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.skelCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.skelCheckBox.setObjectName("skelCheckBox")
        self.gridLayout_2.addWidget(self.skelCheckBox, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 10, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 7, 3, 1, 1)
        self.evalBtn = QtWidgets.QPushButton(self.centralwidget)
        self.evalBtn.setObjectName("evalBtn")
        self.gridLayout_2.addWidget(self.evalBtn, 7, 10, 1, 1)
        self.drawBtn = QtWidgets.QPushButton(self.centralwidget)
        self.drawBtn.setObjectName("drawBtn")
        self.gridLayout_2.addWidget(self.drawBtn, 5, 3, 1, 1)
        self.fileOpenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileOpenBtn.setObjectName("fileOpenBtn")
        self.gridLayout_2.addWidget(self.fileOpenBtn, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 2)
        self.resizeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.resizeCheckBox.setObjectName("resizeCheckBox")
        self.gridLayout_2.addWidget(self.resizeCheckBox, 7, 4, 1, 1)
        self.imgDraw = QtWidgets.QLabel(self.centralwidget)
        self.imgDraw.setText("")
        self.imgDraw.setObjectName("imgDraw")
        self.gridLayout_2.addWidget(self.imgDraw, 1, 1, 1, 3)
        self.knnCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.knnCheckBox.setObjectName("knnCheckBox")
        self.gridLayout_2.addWidget(self.knnCheckBox, 7, 0, 1, 1)
        self.directoryBtn = QtWidgets.QPushButton(self.centralwidget)
        self.directoryBtn.setObjectName("directoryBtn")
        self.gridLayout_2.addWidget(self.directoryBtn, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 7, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 7, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 7, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 7, 9, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 6, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 4, 6, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Monogramm erkennung"))
        self.skelCheckBox.setText(_translate("MainWindow", "Skeletonize"))
        self.evalBtn.setText(_translate("MainWindow", "Auswerten"))
        self.drawBtn.setText(_translate("MainWindow", "Zeichnen"))
        self.fileOpenBtn.setText(_translate("MainWindow", "Durchsuchen"))
        self.resizeCheckBox.setText(_translate("MainWindow", "Resize"))
        self.knnCheckBox.setText(_translate("MainWindow", "KNN"))
        self.directoryBtn.setText(_translate("MainWindow", "Monogram Verzeichnis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

