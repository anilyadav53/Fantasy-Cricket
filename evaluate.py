# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from scoreboard import Ui_Dialog as Score
import sqlite3
match=sqlite3.connect("players_db.db")
matchcur=match.cursor()


class Ui_Dialog(object):
    def __init__(self):
        self.scoreDialog = QtWidgets.QMainWindow
        self.score_screen=Score()
        self.score_screen.setupUi(self.scoreDialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 634)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 200, 211, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget1 = QtWidgets.QListWidget(self.frame)
        self.listWidget1.setGeometry(QtCore.QRect(0, 0, 211, 291))
        self.listWidget1.setObjectName("listWidget1")
        self.verticalScrollBar1 = QtWidgets.QScrollBar(self.frame)
        self.verticalScrollBar1.setGeometry(QtCore.QRect(190, 0, 21, 291))
        self.verticalScrollBar1.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar1.setObjectName("verticalScrollBar1")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(370, 200, 211, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 211, 281))
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.frame_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(190, 0, 21, 281))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.calculatescore = QtWidgets.QPushButton(Dialog)
        self.calculatescore.setGeometry(QtCore.QRect(250, 510, 191, 61))
        self.calculatescore.setStyleSheet("font: 75 14pt \"Arial\";")
        self.calculatescore.setObjectName("calculatescore")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(50, 30, 531, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.ET = QtWidgets.QLabel(self.frame_3)
        self.ET.setGeometry(QtCore.QRect(60, 20, 451, 21))
        self.ET.setStyleSheet("font: 75 14pt \"Arial\";\n"
"font: 75 16pt \"Arial\";")
        self.ET.setObjectName("ET")
        self.comboBox1 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox1.setGeometry(QtCore.QRect(50, 50, 181, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 50, 171, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.players = QtWidgets.QLabel(Dialog)
        self.players.setGeometry(QtCore.QRect(50, 175, 61, 21))
        self.players.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.players.setObjectName("players")
        self.points = QtWidgets.QLabel(Dialog)
        self.points.setGeometry(QtCore.QRect(370, 180, 47, 13))
        self.points.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.points.setObjectName("points")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.calcscore_btn.clicked.connect(self.final_score)
        selected_team = self.selectteam_cb.currentText()

        self.changedname(selected_team)
        self.selectteam_cb.currentTextChanged.connect(self.changedname)

        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calculatescore.setText(_translate("Dialog", "Calculate Score"))
        self.ET.setText(_translate("Dialog", "Evaluate the performance of your fantasy Team"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "match"))
        self.players.setText(_translate("Dialog", "Players"))
        self.points.setText(_translate("Dialog", "Points"))
        self.calcscore_btn.setStatusTip(_translate("Dialog", "calculating score"))
        self.calcscore_btn.setText(_translate("Dialog", "Calculate Score"))


        x = matchcur.execute("SELECT  DISTINCT name from teams;")
        team = x.fetchall()
        for i in team:
            self.selectteam_cb.addItem(i[0])
    def changedname(self, t):
        self.players_lw.clear()
        self.scores_lw.clear()
        y = matchcur.execute("SELECT players from teams WHERE name='" + t + "';")
        player = y.fetchall()
        
        
        for j in player:
            self.players_lw.addItem(j[0])
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            self.scores_lw.addItem(str(k[0]))


    def final_score(self):
        total_score=0
        t=self.selectteam_cb.currentText()
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
       
        
        for k in value:
            total_score+=k[0]
        self.score_screen.finalscore.setText(str(total_score))
        self.scoreDialog.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
