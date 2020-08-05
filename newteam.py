# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 285)
        self.cnt = QtWidgets.QLabel(Dialog)
        self.cnt.setGeometry(QtCore.QRect(100, 40, 231, 41))
        self.cnt.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.cnt.setObjectName("cnt")
        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setGeometry(QtCore.QRect(100, 80, 241, 51))
        self.lineEdit1.setObjectName("lineEdit1")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(140, 180, 121, 51))
        self.save.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.save.setObjectName("save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cnt.setText(_translate("Dialog", "Create New Team"))
        self.lineEdit1.setText(_translate("Dialog", "Enter Team Name"))
        self.save.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
