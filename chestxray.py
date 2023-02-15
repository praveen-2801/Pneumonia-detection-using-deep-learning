import shutil as st
from win32com.client import Dispatch
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from keras import utils
import numpy as np
from keras.applications.vgg16 import preprocess_input
from keras.models import load_model
import tensorflow as tf
import warnings
from PIL import Image, ImageEnhance, ImageTk
import os

warnings.filterwarnings('ignore')


def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 701, 611))
        self.frame.setStyleSheet("background-color: #035874;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, -60, 541, 561))
        self.label.setText("")
        self.gif = QMovie("pnemonia.gif")
        self.label.setMovie(self.gif)
        self.gif.start()
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 430, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border-radius: 10px;\n"
                                      " background-color:#DF582C;\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      " background-color: #7D93E0;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px;\n"
                                        " background-color:#DF582C;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        " background-color: #7D93E0;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.upload_image)
        self.pushButton_2.clicked.connect(self.predict_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "PNEUMONIA Detection Apps"))
        self.label.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p><img src=\"picture.gif\"/></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "PNEUMONIA Detection"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Prediction"))

    def upload_image(self):
        filename = QFileDialog.getOpenFileName()
        global path
        path = filename[0]
        path = str(path)
        print(path)
        model = load_model('chest_xray.h5')
        img_file = utils.load_img(path, target_size=(224, 224))
        x = utils.img_to_array(img_file)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)
        global result
        result = classes
        global name
        name = os.path.basename(path).split('/')[-1]

    def predict_result(self):
        print(result)
        if result[0][0] > 0.5:
            print("Result is Normal")
            speak("Result is Normal")
            original = path
            path2 = f"C:\\Users\Praveen poosa\\OneDrive\\Desktop\\praveen\\project\\chest_xray\\train\\NORMAL\\{name}"
            target = path2
            st.copyfile(original, target)
            print("file added")

        else:
            print("Affected By PNEUMONIA")
            speak("Affected By PNEUMONIA")
            original = path
            path2 = f"C:\\Users\Praveen poosa\\OneDrive\\Desktop\\praveen\\project\\chest_xray\\train\\PNEUMONIA\\{name}"
            target = path2
            st.copyfile(original, target)
            print("file added")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
