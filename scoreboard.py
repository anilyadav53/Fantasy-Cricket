# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoreboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.yts = QtWidgets.QLabel(Dialog)
        self.yts.setGeometry(QtCore.QRect(80, 40, 171, 16))
        self.yts.setStyleSheet("font: 75 14pt \"Arial\";")
        self.yts.setObjectName("yts")
        self.score = QtWidgets.QLabel(Dialog)
        self.score.setGeometry(QtCore.QRect(120, 80, 131, 16))
        self.score.setObjectName("score")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.yts.setText(_translate("Dialog", "Your Team Score:"))
        self.score.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
