from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainApp (object):

    def panel(self,dialog):
        #super(MainApp, self).__init__()
        #self.setStyleSheet('background-color:white;color:black')
        dialog.setObjectName("dialog")
        dialog.resize(812, 632)
        dialog.setStyleSheet("background-color: rgb(0, 170, 255);")
        ## Buttons ##
        self.btn1 = QPushButton("add freind")
        self.btn2 = QPushButton('list freind')
        self.btn3 = QPushButton('2 player')
        self.btn4 = QPushButton('4 player')
        self.btn5 = QPushButton('team player')

        ## Labels ##
        self.lbl1 = QLabel ('متن ۱')
        self.lbl2 = QLabel('متن ۲')

        ## Locations ##
        self.lbl1.setGeometry(2,2,100,70)
        self.layout().addWidget(self.lbl1)

        self.lbl2.setGeometry(2, 50, 100, 70)
        self.layout().addWidget(self.lbl2)

        self.btn1.setGeometry(348,15,100,30)
        self.layout().addWidget(self.btn1)

        self.btn2.setGeometry(348, 70, 100, 30)
        self.layout().addWidget(self.btn2)

        self.btn5.setGeometry(2, 550, 140, 30)
        self.layout().addWidget(self.btn5)

        self.btn4.setGeometry(152, 550, 140, 30)
        self.layout().addWidget(self.btn4)

        self.btn3.setGeometry(152+150, 550, 140, 30)
        self.layout().addWidget(self.btn3)

        ## Resize the window ##
        #self.dialog.resize(450,600)

#app = QtWidgets.QApplication(sys.argv)
#dialog = QtWidgets.QDialog()
#ui = MainApp()
#ui.panel(dialog)
#dialog.show()
#sys.exit(app.exec_())
