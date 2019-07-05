# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(864, 645)
        self.selectImage_btn = QtGui.QPushButton(Dialog)
        self.selectImage_btn.setGeometry(QtCore.QRect(380, 50, 99, 27))
        self.selectImage_btn.setObjectName(_fromUtf8("selectImage_btn"))
        self.result = QtGui.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(400, 610, 68, 17))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        self.image = QtGui.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(250, 120, 381, 331))
        self.image.setObjectName(_fromUtf8("image"))
        self.predict_btn = QtGui.QPushButton(Dialog)
        self.predict_btn.setGeometry(QtCore.QRect(380, 560, 99, 27))
        self.predict_btn.setObjectName(_fromUtf8("predict_btn"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectImage_btn.setText(_translate("Dialog", "Select Image", None))
        self.predict_btn.setText(_translate("Dialog", "Predict", None))


