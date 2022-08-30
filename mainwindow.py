from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_prev = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.gridLayout_2.addWidget(self.pushButton_prev, 0, 0, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout_2.addWidget(self.pushButton_next, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 15, 0, 44)
        self.gridLayout.setHorizontalSpacing(38)
        self.gridLayout.setVerticalSpacing(24)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 8)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuinterface_Alfa = QtWidgets.QMenu(self.menubar)
        self.menuinterface_Alfa.setObjectName("menuinterface_Alfa")
        self.menuinterface_Alfa.setStyleSheet(
                                               "QMenu::item{"
                                               "background-color: rgb(255, 255, 255);"
                                               "color: rgb(0, 0, 0);"
                                               "}"
                                               "QMenu::item:selected{"
                                               "background-color: rgb(0, 85, 127);"
                                               "color: rgb(255, 255, 255);"
                                               "}")

        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action")
        self.menuinterface_Alfa.addAction(self.action)
        self.menuinterface_Alfa.addAction(self.action_2)
        self.menuinterface_Alfa.addAction(self.action_3)
        self.menubar.addAction(self.menuinterface_Alfa.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuinterface_Alfa.setTitle(_translate("MainWindow", "File"))
        self.action.setText(_translate("MainWindow", "Photo Folder"))
        self.action_2.setText(_translate("MainWindow", "Exit Folder"))
        self.action_3.setText(_translate("MainWindow", "Edit Config"))
        self.pushButton_prev.setText(_translate("MainWindow", "Prev[T]"))
        self.pushButton_next.setText(_translate("MainWindow", "Next[G]"))


