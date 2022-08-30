import os
import sys
from mainwindow import *
from os import listdir
import cv2
import tkinter
from tkinter import filedialog
import json
import resources
import shutil

class FunctionalMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # Functional MainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.photo_in_folder = QtWidgets.QLabel(self.groupBox)
        self.photo_in_folder.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo_in_folder.sizePolicy().hasHeightForWidth())
        self.photo_in_folder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.photo_in_folder.setFont(font)
        self.photo_in_folder.setTabletTracking(False)
        self.photo_in_folder.setAcceptDrops(False)
        self.photo_in_folder.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.photo_in_folder.setFrameShadow(QtWidgets.QFrame.Plain)
        self.photo_in_folder.setLineWidth(0)
        self.photo_in_folder.setMidLineWidth(0)
        self.photo_in_folder.setTextFormat(QtCore.Qt.AutoText)
        self.photo_in_folder.setScaledContents(False)
        self.photo_in_folder.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_in_folder.setWordWrap(False)
        self.photo_in_folder.setIndent(-1)
        self.photo_in_folder.setOpenExternalLinks(False)
        self.photo_in_folder.setObjectName("photo_in_folder")
        self.gridLayout.addWidget(self.photo_in_folder, 0, 0, 1, 1)
        self.processed_photos = QtWidgets.QLabel(self.groupBox)
        self.processed_photos.setObjectName("processed_photos")
        font = QtGui.QFont()
        font.setPointSize(17)
        self.processed_photos.setFont(font)
        self.processed_photos.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.processed_photos, 0, 2, 1, 1)
        self.count = -1
        self.count_processed_photo = 0
        self.count_names = 1
        self.pushButton_next.clicked.connect(lambda: self.next("+"))
        self.pushButton_prev.clicked.connect(lambda: self.next("-"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label)
        self.action.triggered.connect(self.photo_folder)
        self.action_2.triggered.connect(self.exit_folder)
        self.action_3.triggered.connect(self.edit_config)
        self.path_config_file = f"C:\\Users\\{os.environ.get('USERNAME')}\\Documents\\PhotoLabeling.txt"
        if not os.path.exists(self.path_config_file):
            root = tkinter.Tk()
            root.withdraw()
            create_file = open(self.path_config_file, "w")
            data_config = dict(photos_folder="", path_exit_folder="", resize=True, resize_resolution=(1280,720), del_photo_name=False,
                               list_category=["1","2","3","4","5","6","7","8","9","10","11","12"])
            create_file.write(json.dumps(data_config, sort_keys=True, indent=4))
            create_file.close()

        read_file = open(self.path_config_file, "r")
        json_read = json.load(read_file)
        read_file.close()
        self.path_photo_folder = json_read["photos_folder"]
        self.path_exit_folder = json_read["path_exit_folder"]
        self.rename_buttons()
        self.pushButton.clicked.connect(lambda: self.sort_photo(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.sort_photo(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.sort_photo(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.sort_photo(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.sort_photo(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.sort_photo(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.sort_photo(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.sort_photo(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.sort_photo(self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(lambda: self.sort_photo(self.pushButton_10.text()))
        self.pushButton_11.clicked.connect(lambda: self.sort_photo(self.pushButton_11.text()))
        self.pushButton_12.clicked.connect(lambda: self.sort_photo(self.pushButton_12.text()))
        self.cur_image = ""
        self.next("+")
        self.count_photo_in_folder = 0
        self.processed_photos.setText(f"Processed Photo    {self.count_processed_photo}")
        self.photo_in_folder.setText(f"Photo in Folder    {self.count_photo_in_folder}")


    def next(self, sign):
        try:
            extension = self.cur_image.split(".")[-1]
            read_file = open(self.path_config_file, "r")
            json_read = json.load(read_file)
            read_file.close()
            photo = listdir(self.path_photo_folder)
            path_temp = f"C:\\Users\\{os.environ.get('USERNAME')}\\Documents"
            if not os.path.exists(f"{path_temp}\\temp"):
                os.makedirs(f"{path_temp}\\temp")
            self.cur_image = f"{self.path_photo_folder}\\{photo[self.count]}"
            res = cv2.imread(self.cur_image)
            width, height, tool = res.shape
            if json_read["resize"] == True:
                temp_photo = f"{path_temp}\\temp\\temp_photo.jpg"
                if width < json_read["resize_resolution"][0] and height < json_read["resize_resolution"][1]:
                    img = cv2.imread(f"{self.path_photo_folder}\\{photo[self.count]}", cv2.IMREAD_UNCHANGED)
                    cv2.imwrite(temp_photo, img)
                    cv2.destroyAllWindows()
                    pixmap = QtGui.QPixmap(temp_photo)
                    self.label.setPixmap(pixmap)
                else:
                    img = cv2.imread(f"{self.path_photo_folder}\\{photo[self.count]}", cv2.IMREAD_UNCHANGED)
                    cv2.imwrite(temp_photo, cv2.resize(img, json_read["resize_resolution"], interpolation=cv2.INTER_AREA))
                    cv2.destroyAllWindows()
                    pixmap = QtGui.QPixmap(temp_photo)
                    self.label.setPixmap(pixmap)
            else:
                pixmap = QtGui.QPixmap(self.cur_image)
                self.label.setPixmap(pixmap)
            if sign == "+":
                self.count += 1
            else:
                self.count -= 1
        except Exception as err:
            print("next: ", err)
            self.count = 0


    def photo_folder(self):
        try:
            root = tkinter.Tk()
            root.withdraw()
            self.path_photo_folder = filedialog.askdirectory()
            read_file = open(self.path_config_file, "r")
            json_read = json.load(read_file)
            read_file.close()
            json_read["photos_folder"] = self.path_photo_folder
            change_file = open(self.path_config_file, "w")
            change_file.write(json.dumps(json_read, sort_keys=True, indent=4))
            change_file.close()
        except Exception as err:
            print("photo_folder: ", err)

    def exit_folder(self):
        root = tkinter.Tk()
        root.withdraw()
        self.path_exit_folder = filedialog.askdirectory()
        read_file = open(self.path_config_file, "r")
        json_read = json.load(read_file)
        read_file.close()
        json_read["path_exit_folder"] = self.path_exit_folder
        change_file = open(self.path_config_file, "w")
        change_file.write(json.dumps(json_read, sort_keys=True, indent=4))
        change_file.close()

    def edit_config(self):
        os.system(self.path_config_file)
        self.rename_buttons()
    def rename_buttons(self):
        try:
            read_file = open(self.path_config_file, "r")
            json_read = json.load(read_file)
            read_file.close()
            self.pushButton.setText(str(json_read["list_category"][0])+"[Q]")
            self.pushButton_2.setText(str(json_read["list_category"][1])+"[W]")
            self.pushButton_3.setText(str(json_read["list_category"][2])+"[E]")
            self.pushButton_10.setText(str(json_read["list_category"][3])+"[R]")
            self.pushButton_4.setText(str(json_read["list_category"][4])+"[A]")
            self.pushButton_5.setText(str(json_read["list_category"][5])+"[S]")
            self.pushButton_6.setText(str(json_read["list_category"][6])+"[D]")
            self.pushButton_11.setText(str(json_read["list_category"][7])+"[F]")
            self.pushButton_7.setText(str(json_read["list_category"][8])+"[Z]")
            self.pushButton_8.setText(str(json_read["list_category"][9])+"[X]")
            self.pushButton_9.setText(str(json_read["list_category"][10])+"[C]")
            self.pushButton_12.setText(str(json_read["list_category"][11])+"[V]")
        except Exception as err:
            print("rename_buttons: ", err)
            read_file = open(self.path_config_file, "r")
            json_read = json.load(read_file)
            read_file.close()
            self.pushButton.setText(json_read["list_category"][0])
            self.pushButton_2.setText(json_read["list_category"][1])
            self.pushButton_3.setText(json_read["list_category"][2])
            self.pushButton_10.setText(json_read["list_category"][3])
            self.pushButton_4.setText(json_read["list_category"][4])
            self.pushButton_5.setText(json_read["list_category"][5])
            self.pushButton_6.setText(json_read["list_category"][6])
            self.pushButton_11.setText(json_read["list_category"][7])
            self.pushButton_7.setText(json_read["list_category"][8])
            self.pushButton_8.setText(json_read["list_category"][9])
            self.pushButton_9.setText(json_read["list_category"][10])
            self.pushButton_12.setText(json_read["list_category"][11])

    def sort_photo(self, name_but):
        try:
            name_but = name_but[:-3]
            extension = self.cur_image.split(".")[-1]
            name_img = self.cur_image.split("\\")[-1]
            read_file = open(self.path_config_file, "r")
            json_read = json.load(read_file)
            read_file.close()
            destination = json_read["path_exit_folder"] + f"\\{name_but}"
            if not os.path.exists(destination):
                os.makedirs(destination)
            shutil.move(self.cur_image, destination)
            if json_read["del_photo_name"] == False:
                shutil.move(destination+f"\\{name_img}", destination+f"\\{name_but}_{name_img}")
            else:
                shutil.move(destination + f"\\{name_img}", destination + f"\\{name_but}_{self.count_names}.{extension}")
            self.count = 0
            self.count_processed_photo += 1
            self.count_photo_in_folder = len(listdir(self.path_photo_folder))
            self.next("+")
            self.processed_photos.setText(f"Processed Photo   {self.count_processed_photo}")
            self.photo_in_folder.setText(f"Photo in Folder   {self.count_photo_in_folder}")
        except Exception as err:
            print("sort_photo: ", err)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Q:
            self.sort_photo(self.pushButton.text())
        elif e.key() == QtCore.Qt.Key_W:
            self.sort_photo(self.pushButton_2.text())
        elif e.key() == QtCore.Qt.Key_E:
            self.sort_photo(self.pushButton_3.text())
        elif e.key() == QtCore.Qt.Key_R:
            self.sort_photo(self.pushButton_10.text())
        elif e.key() == QtCore.Qt.Key_A:
            self.sort_photo(self.pushButton_4.text())
        elif e.key() == QtCore.Qt.Key_S:
            self.sort_photo(self.pushButton_5.text())
        elif e.key() == QtCore.Qt.Key_D:
            self.sort_photo(self.pushButton_6.text())
        elif e.key() == QtCore.Qt.Key_F:
            self.sort_photo(self.pushButton_11.text())
        elif e.key() == QtCore.Qt.Key_Z:
            self.sort_photo(self.pushButton_7.text())
        elif e.key() == QtCore.Qt.Key_X:
            self.sort_photo(self.pushButton_8.text())
        elif e.key() == QtCore.Qt.Key_C:
            self.sort_photo(self.pushButton_9.text())
        elif e.key() == QtCore.Qt.Key_V:
            self.sort_photo(self.pushButton_12.text())
        elif e.key() == QtCore.Qt.Key_G:
            self.next("+")
        elif e.key() == QtCore.Qt.Key_T:
            self.next("-")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FunctionalMainWindow()
    ui.setupUi(MainWindow)
    ui.show()
    ui.setWindowTitle("Photo Labeling")
    ui.setWindowIcon(QtGui.QIcon(':/mainico/PhotoLabeling.ico'))
    sys.exit(app.exec_())