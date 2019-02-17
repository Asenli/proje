# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseShow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit, QFileDialog

from python35 import qq_data

class Ui_Form(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("QQ批量登录")
        Form.resize(427, 253)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 100, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 91, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 50, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 100, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QQ批量登录"))
        self.pushButton.setText(_translate("Form", "开始登录"))
        self.label.setText(_translate("Form", "QQ路径："))
        self.label_2.setText(_translate("Form", "输入文本路径："))
        self.pushButton_2.setText(_translate("Form", "选择文件"))
        self.pushButton_3.setText(_translate("Form", "选择文件"))
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.pushButton_2.clicked.connect(self.setValue)
        self.pushButton_3.clicked.connect(self.setValue2)
        self.pushButton.clicked.connect(self.get_path)

    def setValue(self):
        # 获取框一的值并填进去
        QQ_path = self.showDialog1()
        self.lineEdit.setText(QQ_path)

    def setValue2(self):
        Txt_path = self.showDialog2()
        self.lineEdit_2.setText(Txt_path)

    def showDialog1(self):
        """
        打开选择文件 返回路径
        :return:
        """
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取QQ程序",
                                                          "C:/",
                                                          " Files (*.exe)")  #
        print(fileName1, filetype)
        return fileName1

    def showDialog2(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文本",
                                                          "C:/",
                                                          "All Files (*.txt)")  #
        # fname = QFileDialog.getOpenFileName(self, 'open file', '/')
        print(fileName1)
        return fileName1


    def get_path(self):
        qq_path = self.lineEdit.text()
        txt_path = self.lineEdit_2.text()

        qq_data(txt_path, qq_path)
        print(qq_path,txt_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
