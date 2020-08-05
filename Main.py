# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from calculate_points import player_points
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from open import Ui_Dialog as open
from newteam import Ui_Dialog as New
from evaluate import Ui_Dialog as evaluate


import sqlite3
calc=sqlite3.connect('player.db')
calccurs=calc.cursor()



class Ui_MainWindow(object):
    def __init__(self):
        self.newDialog=QtWidgets.QMainWindows()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)

    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()




        


        
    def setupUi(self, MainWindow):

        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0

        self.a = []  
        self.b = [] 
        self.c = []   
        self.d = []  
        self.list1 = []    
    

        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 615)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 621, 111))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ys = QtWidgets.QLabel(self.frame)
        self.ys.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.ys.setObjectName("ys")
        self.bat = QtWidgets.QLabel(self.frame)
        self.bat.setGeometry(QtCore.QRect(10, 26, 71, 20))
        self.bat.setObjectName("bat")
        self.bat1 = QtWidgets.QLabel(self.frame)
        self.bat1.setGeometry(QtCore.QRect(80, 30, 47, 13))
        self.bat1.setStyleSheet("")
        self.bat1.setObjectName("bat1")
        self.bow = QtWidgets.QLabel(self.frame)
        self.bow.setGeometry(QtCore.QRect(120, 26, 71, 20))
        self.bow.setObjectName("bow")
        self.bow1 = QtWidgets.QLabel(self.frame)
        self.bow1.setGeometry(QtCore.QRect(200, 30, 47, 13))
        self.bow1.setObjectName("bow1")
        self.ar = QtWidgets.QLabel(self.frame)
        self.ar.setGeometry(QtCore.QRect(270, 20, 81, 31))
        self.ar.setObjectName("ar")
        self.ar1 = QtWidgets.QLabel(self.frame)
        self.ar1.setGeometry(QtCore.QRect(370, 20, 21, 31))
        self.ar1.setObjectName("ar1")
        self.wk = QtWidgets.QLabel(self.frame)
        self.wk.setGeometry(QtCore.QRect(430, 20, 101, 31))
        self.wk.setObjectName("wk")
        self.wk1 = QtWidgets.QLabel(self.frame)
        self.wk1.setGeometry(QtCore.QRect(540, 30, 47, 13))
        self.wk1.setObjectName("wk1")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 120, 621, 71))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PA = QtWidgets.QLabel(self.frame_2)
        self.PA.setObjectName("PA")
        self.horizontalLayout.addWidget(self.PA)
        self.PA1 = QtWidgets.QLabel(self.frame_2)
        self.PA1.setObjectName("PA1")
        self.horizontalLayout.addWidget(self.PA1)
        self.PU = QtWidgets.QLabel(self.frame_2)
        self.PU.setObjectName("PU")
        self.horizontalLayout.addWidget(self.PU)
        self.PU1 = QtWidgets.QLabel(self.frame_2)
        self.PU1.setObjectName("PU1")
        self.horizontalLayout.addWidget(self.PU1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 621, 341))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 261, 291))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setGeometry(QtCore.QRect(10, 0, 251, 291))
        self.listWidget.setObjectName("listWidget")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(289, -1, 281, 291))
        self.frame_5.setStyleSheet("border-color: rgb(10, 9, 9);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_5)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 281, 291))
        self.listWidget_2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.TN = QtWidgets.QLabel(self.frame_7)
        self.TN.setGeometry(QtCore.QRect(20, 5, 81, 21))
        self.TN.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.TN.setObjectName("TN")
        self.DH = QtWidgets.QLabel(self.frame_7)
        self.DH.setGeometry(QtCore.QRect(110, 0, 101, 31))
        self.DH.setStyleSheet("")
        self.DH.setObjectName("DH")
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(20, 209, 241, 31))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton1 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton1.setObjectName("radioButton1")
        self.horizontalLayout_3.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout_3.addWidget(self.radioButton2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_3.addWidget(self.radioButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.actionNew_Team.triggered.connect(self.file_new)
        self.actionOpen_Team.triggered.connect(self.file_open)
        self.actionSave_Team.triggered.connect(self.file_save)
        self.actionEvaluate_Team.triggered.connect(self.file_evaluate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.PA.itemDoubleClicked.connect(self.removelist1)
        self.PA1.itemDoubleClicked.connect(self.removelist2)


        self.stats={}
        self.new_screen.savename.clicked.connect(self.namechange)


        self.radiobutton1.clicked.connect(self.load_names)
        self.radiobutton2.connect(self.load_names)
        self.radiobutton4.connect(self.load_names)
        self.radiobutton5.connect(self.load_names)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ys.setText(_translate("MainWindow", "Your Selections"))
        self.bat.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.bat1.setText(_translate("MainWindow", "##"))
        self.bow.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.bow1.setText(_translate("MainWindow", "##"))
        self.ar.setText(_translate("MainWindow", "Alrounders(AR)"))
        self.ar1.setText(_translate("MainWindow", "##"))
        self.wk.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.wk1.setText(_translate("MainWindow", "##"))
        self.PA.setText(_translate("MainWindow", "Points Available"))
        self.PA1.setText(_translate("MainWindow", "####"))
        self.PU.setText(_translate("MainWindow", "Points Used "))
        self.PU1.setText(_translate("MainWindow", "####"))
        self.TN.setText(_translate("MainWindow", "Team Name"))
        self.DH.setText(_translate("MainWindow", "Displayed Here"))
        self.radioButton1.setText(_translate("MainWindow", "BAT"))
        self.radioButton2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_4.setText(_translate("MainWindow", "AR"))
        self.radioButton_5.setText(_translate("MainWindow", "WK"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))

    def file_new(self):
        self.newDialog.show()

    def namechange(self):
        teamname = self.new_screen.team_name.text()
        fantcurs.execute("SELECT DISTINCT name FROM teams")
        l = fantcurs.fetchall()
        for i in l:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.team_name.text()
            self.team_name.setText(str('    '+self.tname))
            self.newDialog.close()

    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.sel_player.clear()


    

    def file_save(self):
        if not self.error():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(' Inufficient Players OR Points !!')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error():
            try:
                fantcurs.execute("SELECT DISTINCT name FROM teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.team_name.text() == i[0]:
                        print('Updating already there')
                        fantcurs.execute("DELETE  FROM teams WHERE name='" + self.team_name.text() + "';")

            except:
                print('error')
            for i in range(self.sel_player.count()):
                
                try:
                    fantcurs.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.team_name.text(), self.list1[i], player_points[self.list1[i]]))

                    
                except:
                    print('error in operation!')
            fant.commit()
        else:
            print('---error in operation')


     def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT player,value from stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,value from stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,value from stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,value from stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)

        elif self.wk_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)

    def removelist1(self, item):   
        self.conditions_1(item.text())
        self.av_player.takeItem(self.av_player.row(item))
        self.sel_player.addItem(item.text())
        self.totalcount = self.sel_player.count()
        self.list1.append(item.text())
        self.error()

    def conditions_1(self, cat):   
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))

    def conditions_2(self, cat):   
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))

    def removelist2(self, item):
        self.sel_player.takeItem(self.sel_player.row(item))
        self.av_player.addItem(item.text())
        self.list1.remove(item.text())
        self.totalcount = self.sel_player.count()
        self.conditions_2(item.text())

    def openteam(self):
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.team_name.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        x=fantcurs.fetchall()
        score=[]
        for i in x:
            fantcurs.execute("SELECT value from stats WHERE player='"+i[0]+"';")
            y=fantcurs.fetchone()
            score.append(y[0])
        
        sum=0
        for i in score:
            sum+=i
        self.sel_player.clear()
        self.load_names()
        for i in x:
            self.sel_player.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def enablebuttons(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)
        
    def disablebuttons(self):
        self.bat_rb.setEnabled(False)
        self.bow_rb.setEnabled(False)
        self.ar_rb.setEnabled(False)
        self.wk_rb.setEnabled(False)
        

    def error(self):
        msg = QMessageBox()
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            return 0
        elif self.totalcount < 11 :
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0

        return 1






        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
