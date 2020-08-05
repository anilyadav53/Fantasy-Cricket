# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
match=sqlite3.connect('players_db.db')
matchcur=match.cursor()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.sto = QtWidgets.QLabel(Dialog)
        self.sto.setGeometry(QtCore.QRect(80, 40, 271, 41))
        self.sto.setStyleSheet("font: 75 14pt \"Arial\";")
        self.sto.setObjectName("sto")
        self.comboBox0pen = QtWidgets.QComboBox(Dialog)
        self.comboBox0pen.setGeometry(QtCore.QRect(80, 100, 161, 31))
        self.comboBox0pen.setObjectName("comboBox0pen")
        self.open = QtWidgets.QPushButton(Dialog)
        self.open.setGeometry(QtCore.QRect(110, 190, 111, 41))
        self.open.setStyleSheet("font: 75 12pt \"Arial\";")
        self.open.setObjectName("open")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        teams=matchcur.execute("SELECT DISTINCT name FROM teams;")
        y=teams.fetchall()
        for i in y:
            self.open_cb.addItem(i[0])


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sto.setText(_translate("Dialog", "Select team to open"))
        self.open.setText(_translate("Dialog", "Open"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
