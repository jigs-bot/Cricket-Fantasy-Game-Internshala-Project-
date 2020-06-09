
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt

import sqlite3


class Ui_MainWindow(QWidget):

#Fetching Data From DataBase On Radio Button Selection
    def show(self,b):
        
        connection = sqlite3.connect("D:\SQLiteStudio-3.2.1\SQLiteStudio\players.db")
        print(str(b.text()))
        if b.isChecked():
            
            category= b.text()
            curschool=connection.cursor()
            curschool.execute("select*from stats where ctg=? ",(category,))
            result=curschool.fetchall()
            self.listWidget.clear()
            for x in result:
                self.listWidget.addItem(str(x[0]))
                #self.listWidget.setAlignment(QtCore.Qt.AlignCenter)
            print(str(result))
        connection.close()

#Adding data from list widget 1 to list widget 2
        
    def list1(self,item):
        
        self.listWidget.takeItem(self.listWidget.row(item))
        self.listWidget_2.addItem(item.text())
        a=item.text()
        print(a)
        connection = sqlite3.connect("D:\SQLiteStudio-3.2.1\SQLiteStudio\players.db")
        curschool=connection.cursor()
        curschool.execute("select * from stats where player=? ",(a,))
        result=curschool.fetchall()
        points=int(self.label_12.text().isdigit())
        print(points)
        
        for x in result:
             
            L1=list(x)
            points=points+ L1[-2]
            
            if(L1[-1]=='BAT'):
                self.label_6.setNum(int(self.label_6.text().isdigit())+1)
                self.label_12.setText(str(points))
            elif(L1[-1]=='WK'):
                self.label_8.setNum(int(self.label_8.text().isdigit())+1)
                self.label_12.setNum(int(self.label_12.text().isdigit())+L1[-2])
            elif(L1[-1]=='AR'):
                self.label_7.setNum(int(self.label_7.text().isdigit())+1)
                self.label_12.setNum(int(self.label_12.text().isdigit())+L1[-2])
            elif(L1[-1]=='BWL'):
                self.label_5.setNum(int(self.label_5.text().isdigit())+1)
                self.label_12.setNum(int(self.label_12.text().isdigit())+L1[-2])
                break

#Removing data from list widget 2   
    def list2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.insertItem(5,item.text())
        print()

#New Team option From File Menu
        
    def called(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            self.label_13.setText(str(text))

        self.listWidget_2.clear()
        self.listWidget.clear()
        self.label_5.clear()
        self.label_6.clear()
        self.label_7.clear()
        self.label_8.clear()
        self.label_12.clear()
#saving Team Stats To the database
        
    def save(self,c,d,e):
        c=self.listWidget_2.count()
        d=self.label_13.text()
        e=self.label_12.text()
        connection = sqlite3.connect("D:\SQLiteStudio-3.2.1\SQLiteStudio\players.db")
        items = []
        for index in range(0,c):
            items.append(self.listWidget.item(index))

        print(items)
        curschool=connection.cursor()
        curschool.execute("insert into teams(name,players,t_value) values(?,?,?)", (d,str(items),e,))
        connection.commit()
        print("recorf inserted")
        connection.close()
        
        
     
            
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 581, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(280, 30, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(430, 30, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(90, 30, 31, 16))
        
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(210, 30, 31, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(360, 30, 31, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(530, 30, 31, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 130, 20, 321))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 120, 581, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 180, 41, 17))
        self.radioButton.setObjectName("radioButton")
        #self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(lambda:self.show(self.radioButton))
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 180, 41, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton.toggled.connect(lambda:self.show(self.radioButton_2))
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 180, 41, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton.toggled.connect(lambda:self.show(self.radioButton_3))
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 180, 51, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton.toggled.connect(lambda:self.show(self.radioButton_4))
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 140, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 140, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 140, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 140, 47, 13))
        self.label_12.setObjectName("label_12")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 170, 256, 281))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.list1)
        
        #self.listWidget.addItem("raam")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(350, 170, 256, 281))
        self.listWidget_2.setObjectName("listWidget_2")
        
        self.listWidget_2.itemDoubleClicked.connect(self.list2)
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(440, 190, 47, 13))
        self.label_13.setObjectName("label_13")
        self.listWidget_2.raise_()
        self.listWidget.raise_()
        self.groupBox.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.radioButton_4.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        #self.label_12.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.called)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(lambda:self.save(self.listWidget_2,self.label_12,self.label_13))
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cricket Fantacy"))
        MainWindow.setStyleSheet(" background-image: url(j.jpg) ;")
        self.groupBox.setTitle(_translate("MainWindow", "Your Selection"))
        self.label.setText(_translate("MainWindow", "Batsman(BAT):"))
        self.label_2.setText(_translate("MainWindow", "Bowler(BOW):"))
        self.label_3.setText(_translate("MainWindow", "All-Rounder(AR):"))
        self.label_4.setText(_translate("MainWindow", "Wicket-Keeper(WK):"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "WK"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "BWL"))
        self.label_9.setText(_translate("MainWindow", "Points Available"))
        self.label_10.setText(_translate("MainWindow", "Points Used"))
        self.label_11.setText(_translate("MainWindow", ""))
        #self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New Team"))
        self.actionNew.setIconText(_translate("MainWindow", "New Team"))
        self.actionOpen.setText(_translate("MainWindow", "Open Team"))
        self.actionSave.setText(_translate("MainWindow", "Save Team"))
        self.actionSave_As.setText(_translate("MainWindow", "Evaluate Team"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
