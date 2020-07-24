from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from database import *
from freindatabase import *
from findplayer import *
from playbasket import *
import time
class MainApp(object):
    def setupUi(self, window,user):
        #super(MainApp, self).__init__()
        self.selected_address = None

        window.setObjectName("panel")

        #if not Dialog.objectName():
        #Dialog.setObjectName(u"Dialog")

        window.setStyleSheet("background-color:black;")

        window.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        #self.frame = QPUS(Dialog)
        #self.frame.setGeometry(QtCore.QRect(90, 80, 631, 461))
        #self.frame.setStyleSheet("background-color:blue;")
        #self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame.setObjectName("frame")
        self.mouz = QtWidgets.QPushButton(self.centralwidget)
        self.mouz.setObjectName("mouz")
        self.mouz.setGeometry(QtCore.QRect(260, 240, 84, 26))
        #self.mouz.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setObjectName("b")
        self.b.setGeometry(QtCore.QRect(130, 240, 84, 26))
        self.pushButton =QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 84, 26))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(200,105, 84, 26))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(270, 50, 84, 26))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QtCore.QRect(200,155, 84, 26))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label1=QtWidgets.QLabel(self.centralwidget)
        self.label2=QtWidgets.QLabel(self.centralwidget)
        self.label3=QtWidgets.QLabel(self.centralwidget)
        #self.label_3.setGeometry(QtCore.QRect(90, 260, 121, 21))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.label_3.setFont(font)
        self.label.setObjectName("label")
        self.label1.setObjectName("label1")
        self.label2.setObjectName("label2")
        self.label2.setGeometry(QtCore.QRect(10,100,110,35))
        self.label3.setObjectName("label3")
        self.label3.setGeometry(QtCore.QRect(10,150,110,35))
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("textEdit")
        self.lineEdit.setGeometry(QtCore.QRect(80,100,110,35))
        self.lineEdit.setStyleSheet("background-color:blue;")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setObjectName("textEdit1")
        self.lineEdit1.setGeometry(QtCore.QRect(80,150,110,35))
        self.lineEdit1.setStyleSheet("background-color:blue;")
        #self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        #self.textEdit_2.setObjectName("textEdit_2")
        self.label1.setGeometry(QtCore.QRect(10, 57, 101, 31))
        window.setCentralWidget(self.centralwidget)

        self.pushButton_2.clicked.connect(lambda:freind(self.lineEdit.text(),user))
        self.pushButton_3.clicked.connect(lambda:show_my_freind(user))
        self.pushButton_4.clicked.connect(lambda:play_freind(self.lineEdit1.text(),user))
        self.mouz.clicked.connect(lambda:game2(user))
        self.b.clicked.connect(lambda:game4(user))
        self.pushButton.clicked.connect(lambda:game44(user))
        self.retranslateUi(window,user)

        QMetaObject.connectSlotsByName(window)
    # setupUi


    def retranslateUi(self, window,user):
        _translate = QCoreApplication.translate
        window.setWindowTitle(QCoreApplication.translate("window", "panel", None))
        lvl=search_lvl(user)
        self.label.setText(QCoreApplication.translate("window", "user : {}".format(user), None))
        self.label1.setText(QCoreApplication.translate("window", "lvl : {}".format(lvl), None))
        self.label2.setText(QCoreApplication.translate("window", "user freind: ", None))
        self.label3.setText(QCoreApplication.translate("window", "user freind: ", None))
        self.mouz.setText(QCoreApplication.translate("window", "play2", None))
        self.b.setText(QCoreApplication.translate("window", "play4", None))
        self.pushButton.setText(QCoreApplication.translate("window", "team", None))
        self.pushButton_2.setText(QCoreApplication.translate("window", "add freind", None))
        self.pushButton_3.setText(QCoreApplication.translate("window", "show freind", None))
        self.pushButton_4.setText(QCoreApplication.translate("window", "play freind", None))

    def update(self,user):
        _translate = QCoreApplication.translate
        lvl=search_lvl(user)
        self.label1.setText(QCoreApplication.translate("window", "lvl : {}".format(lvl), None))

def clear_prepare(user):
    exe_query("UPDATE user SET prepare=0 WHERE name=%s ", (user,), 0)


def play_freind(freind_user,user):
    id_user=search_id(user)
    exist=0
    exist_freind=search_user(freind_user)
    if(exist_freind==False):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("your freind isnt exist")
        error_dialog.exec_()
    else:
        id_freind=search_id(freind_user)
        exist=repeat_freind(id_user, id_freind)

    if(exist!=-1):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("user didnt your freind")
        error_dialog.exec_()

    else:
        lis=[user,id_freind]
        prepare_for_friend(lis)
        time_out=time.time()+30
        #fre=True
        count=0
        while(True):
            prepare=exe_query("SELECT * FROM user WHERE name = %s", freind_user, 1)
            if(prepare[7]==id_user):
                count+=1
                break
            elif(prepare[7]!=0 and prepare[7]!=id_user):
                count-=1
                break
            elif(time.time()>time_out):
                break

        if(count==-1):
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("your freind request for another one")
            error_dialog.exec_()
            end_prepare(user)
        elif(count==0):
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Information)
            error_dialog.setText("your freind didnt request")
            error_dialog.exec_()
            end_prepare(user)
        else:
            #for i in player:
                #exe_query("UPDATE user SET prepare=-1 WHERE name=%s ", (i,), 0)

            lvl=search_lvl(user)
            end_prepare(user)
            score=main(lvl,user)
            #pygame.quit()
            exe_query("UPDATE user SET point=%s WHERE name=%s", (score,user,), 0)
            player=[freind_user,user]
            if(score):
                tim=True
                while(tim):
                    count=0
                    for i in player:
                        temp=check_score(i)
                        if(temp==-1):
                            count+=1
                    if(count==0):
                        tim=False

            time.sleep(15)
            score1=exe_query("SELECT * FROM user WHERE name = %s",(player[0],),1)
            score1=score1[6]
            score2=exe_query("SELECT * FROM user WHERE name = %s",(player[1],),1)
            score2=score2[6]
            #print(score2)
            #print(score1)
            win="win"
            lose="lose"
            same="same"
            if(score1>score2):
                if(user==player[0]):
                    edit_lvl(player[0], 3)
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Information)
                    error_dialog.setText("{} win".format(user))
                    error_dialog.exec_()
                if(user==player[1]):
                    edit_lvl(player[1], -1)
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Information)
                    error_dialog.setText("{} lose".format(user))
                    error_dialog.exec_()
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[0],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[1],), 0)
            elif(score2>score1):
                if(user==player[1]):
                    edit_lvl(player[1], 3)
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Information)
                    error_dialog.setText("{} win".format(user))
                    error_dialog.exec_()
                if(user==player[0]):
                    edit_lvl(player[0], -1)
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Information)
                    error_dialog.setText("{} lose".format(user))
                    error_dialog.exec_()
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[1],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[0],), 0)
            else:
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[1],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[0],), 0)

            time.sleep(3)
            exe_query("UPDATE user SET point=-1 WHERE name=%s ", (user,), 0)
            #MainApp.update(user)



def game44(user):
    prepare_game(user, 44)
    action_find(44)
    player=match_user44(user)
    time_out=time.time()+30
    while(player==-1):
        if(time.time()>time_out):
            clear_prepare(user)
            break
        action_find(44)
        player=match_user44(user)

    if(player==-1):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setText("we cant find player")
        error_dialog.exec_()
    else:

        lvl=search_lvl(user)
        score=main(lvl,user)
        exe_query("UPDATE user SET point=%s WHERE name=%s", (score,user,), 0)
        if(score):
            tim=True
            while(tim):
                count=0
                for i in player:
                    temp=check_score(i)
                    if(temp==-1):
                        count+=1
                if(count==0):
                    tim=False
            time.sleep(15)
            score1=exe_query("SELECT * FROM user WHERE name = %s",(player[0],),1)
            score1=score1[6]
            score2=exe_query("SELECT * FROM user WHERE name = %s",(player[1],),1)
            score2=score2[6]
            score3=exe_query("SELECT * FROM user WHERE name = %s",(player[2],),1)
            score3=score3[6]
            score4=exe_query("SELECT * FROM user WHERE name = %s",(player[3],),1)
            score4=score4[6]
            win="win"
            lose="lose"
            same="same"
            team_1=score1+score2
            team_2=score3+score4
            if(team_1>team_2):
                if(user==player[0] or user==player[1]):
                    if(user==player[0]):
                        edit_lvl(player[0], 4)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} win".format(user))
                        error_dialog.exec_()
                    else:
                        edit_lvl(player[1], 4)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} win".format(user))
                        error_dialog.exec_()
                if(user==player[2] or user==player[3]):
                    if(user==player[2]):
                        edit_lvl(player[2], -1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} lose".format(user))
                        error_dialog.exec_()
                    else:
                        edit_lvl(player[3], -1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} lose".format(user))
                        error_dialog.exec_()
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[0],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[1],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[2],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[3],), 0)
            elif(team_1<team_2):
                if(user==player[0] or user==player[1]):
                    if(user==player[0]):
                        edit_lvl(player[0], -1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} lose".format(user))
                        error_dialog.exec_()
                    else:
                        edit_lvl(player[1], -1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} lose".format(user))
                        error_dialog.exec_()
                if(user==player[2] or user==player[3]):
                    if(user==player[2]):
                        edit_lvl(player[2], 4)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} win".format(user))
                        error_dialog.exec_()
                    else:
                        edit_lvl(player[3], 4)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} win".format(user))
                        error_dialog.exec_()
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[3],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[2],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[1],), 0)
                exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[0],), 0)
            else:
                if(user==player[0] or user==player[1] or user==player[2] or user):
                    if(user==player[0]):
                        edit_lvl(player[0], 1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} same".format(user))
                        error_dialog.exec_()
                    elif(user==player[1]):
                        edit_lvl(player[1], 1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} same".format(user))
                        error_dialog.exec_()
                    elif(user==player[2]):
                        edit_lvl(player[2], 1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} same".format(user))
                        error_dialog.exec_()
                    else:
                        edit_lvl(player[3], 1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} same".format(user))
                        error_dialog.exec_()
                    exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[3],), 0)
                    exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[2],), 0)
                    exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[1],), 0)
                    exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[0],), 0)
            time.sleep(3)
            exe_query("UPDATE user SET point=-1 WHERE name=%s ", (user,), 0)


def game4(user):
    prepare_game(user, 4)
    action_find(4)
    player=match_user4(user)
    time_out=time.time()+30
    while(player==-1):
        if(time.time()>time_out):
            clear_prepare(user)
            break
        action_find(4)
        player=match_user4(user)
    if(player==-1):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setText("we cant find player")
        error_dialog.exec_()
    else:


        lvl=search_lvl(user)
        score=main(lvl,user)
        exe_query("UPDATE user SET point=%s WHERE name=%s", (score,user,), 0)
        if(score):
            tim=True
            while(tim):
                count=0
                for i in player:
                    temp=check_score(i)
                    if(temp==-1):
                        count+=1
                if(count==0):
                    tim=False
        time.sleep(15)
        score1=exe_query("SELECT * FROM user WHERE name = %s",(player[0],),1)
        score1=score1[6]
        score2=exe_query("SELECT * FROM user WHERE name = %s",(player[1],),1)
        score2=score2[6]
        score3=exe_query("SELECT * FROM user WHERE name = %s",(player[2],),1)
        score3=score3[6]
        score4=exe_query("SELECT * FROM user WHERE name = %s",(player[3],),1)
        score4=score4[6]
        win="win"
        lose="lose"
        same="same"
        all_score=[score1,score2,score3,score4]
        if(score1==score2==score3==score4):
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Information)
            error_dialog.setText("{} same".format(user))
            error_dialog.exec_()
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[1],), 0)
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[0],), 0)
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[2],), 0)
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[3],), 0)
        else:
            max=score1
            count=0
            for i in all_score:
                if(i>score1):
                    max=i
                    pos=count
                count+=1

            for s in range(4):
                if(s==count and user==player[s]):
                    edit_lvl(player[s], 3)
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Information)
                    error_dialog.setText("{} win".format(user))
                    error_dialog.exec_()
                    exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[s],), 0)
                else:
                    if(user==player[s]):
                        edit_lvl(player[s], -1)
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Information)
                        error_dialog.setText("{} lose".format(user))
                        error_dialog.exec_()
                        exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[s],), 0)
        time.sleep(3)
        exe_query("UPDATE user SET point=-1 WHERE name=%s ", (user,), 0)


def game2(user):
    prepare_game(user, 2)
    action_find(2)
    player=match_user2(user)
    time_out=time.time()+30
    while(player==-1):
        if(time.time()>time_out):
            clear_prepare(user)
            break
        #search=exe_query("SELECT * FROM user WHERE name = %s",(user,),1)
        action_find(2)
        player=match_user2(user)
    if(player==-1):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setText("we cant find player")
        error_dialog.exec_()
    else:
        #for i in player:
            #exe_query("UPDATE user SET prepare=-1 WHERE name=%s ", (i,), 0)\
        lvl=search_lvl(user)
        score=main(lvl,user)
        #pygame.quit()
        exe_query("UPDATE user SET point=%s WHERE name=%s", (score,user,), 0)
        if(score):
            tim=True
            while(tim):
                count=0
                for i in player:
                    temp=check_score(i)
                    if(temp==-1):
                        count+=1
                if(count==0):
                    tim=False
        time.sleep(15)
        score1=exe_query("SELECT * FROM user WHERE name = %s",(player[0],),1)
        score1=score1[6]
        score2=exe_query("SELECT * FROM user WHERE name = %s",(player[1],),1)
        score2=score2[6]
        #print(score2)
        #print(score1)
        win="win"
        lose="lose"
        same="same"
        if(score1>score2):
            if(user==player[0]):
                edit_lvl(player[0], 3)
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Information)
                error_dialog.setText("{} win".format(user))
                error_dialog.exec_()
            if(user==player[1]):
                edit_lvl(player[1], -1)
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Information)
                error_dialog.setText("{} lose".format(user))
                error_dialog.exec_()
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[0],), 0)
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[1],), 0)
        elif(score2>score1):
            if(user==player[1]):
                edit_lvl(player[1], 3)
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Information)
                error_dialog.setText("{} win".format(user))
                error_dialog.exec_()
            if(user==player[0]):
                edit_lvl(player[0], -1)
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Information)
                error_dialog.setText("{} lose".format(user))
                error_dialog.exec_()
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (win,player[1],), 0)
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (lose,player[0],), 0)
        else:
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[1],), 0)
            exe_query("UPDATE user SET lastgame=%s WHERE name=%s ", (same,player[0],), 0)

        time.sleep(3)
        exe_query("UPDATE user SET point=-1 WHERE name=%s ", (user,), 0)
        #MainApp.update(user)



def show_my_freind(user):
    id_user=search_id(user)
    my_freind=show_freind(id_user)
    if(my_freind):
        list_freind=""
        for i in my_freind:
            temp=i[1]
            user_freind=show_user(temp)
            list_freind+=user_freind+","
        msgbox = QMessageBox()
        msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
        msgbox.setWindowTitle("freind")
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setText("all freind:  ")
        msgbox.setDetailedText( "%s\n" % list_freind)
        msgbox.exec_()
    else:
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setText("you dont have freind")
        error_dialog.exec_()

def freind(user_freind,user):
    id_user=search_id(user)
    freind_exist=search_user(user_freind)
    if(freind_exist==False):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("your freind not exist")
        error_dialog.exec_()
    else:
        id_freind=search_id(user_freind)
        repeat=repeat_freind(id_user, id_freind)
        if(repeat==-1):
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("this user is already your freind")
            error_dialog.exec_()
        else:
            add_freind(id_user,id_freind)
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Information)
            error_dialog.setText("your freind add")
            error_dialog.exec_()

class Ui_Dialog(object):
    #switch_window = QtCore.pyqtSignal()
    #def __init_(self):

        #super(Ui_Dialog, self).__init__()

    def login(self,user):
        #print('looggggggg!')
        #QCoreApplication.quit()
        #app = QtWidgets.QApplication(sys.argv)
        #Dialog = QtWidgets.QDialog()
        self.ui = MainApp()
        self.ui.setupUi(Dialog,user)
        Dialog.show()
        #ui.show()
        #Dialog.show()
        #sys.exit(app.exec_())
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 632)
        Dialog.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        #self.frame = QPUS(self.centralwidget)
        #self.frame.setGeometry(QtCore.QRect(90, 80, 631, 461))
        #self.frame.setStyleSheet("background-color:blue;")
        #self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 80, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 190, 231, 31))
        self.lineEdit.setStyleSheet("background-color: black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 260, 231, 31))
        self.lineEdit_2.setStyleSheet("background-color:black;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 360, 101, 41))
        self.pushButton_2.setStyleSheet("background-color:yellow;")
        self.pushButton_2.setObjectName("pushButton_2")
        Dialog.setCentralWidget(self.centralwidget)
        self.count=-2
        self.pushButton.clicked.connect(lambda:check_user())
        self.pushButton_2.clicked.connect(lambda:sign_up())
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Log in Form"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Log in"))
        self.pushButton_2.setText(_translate("Dialog", "Sign up"))
def check_user():
    _translate = QCoreApplication.translate
    ui.label.setText(_translate("Dialog", "Log in Form"))
    if(ui.count==-1):
        ui.count=-2
        return
    user_exist=search_user(ui.lineEdit.text())
    if(user_exist==True):
        check_pass=search_login(ui.lineEdit.text(), ui.lineEdit_2.text())
        if(check_pass==True):
            lvl=search_lvl(ui.lineEdit.text())

    if(user_exist==False):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("the user is not exist")
        error_dialog.exec_()
        ui.lineEdit.setText("")
        ui.lineEdit_2.setText("")
    elif(check_pass==False):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("your password is wrong")
        error_dialog.exec_()
        ui.lineEdit.setText("")
        ui.lineEdit_2.setText("")
    else:
        ui.login(ui.lineEdit.text())
            #QCoreApplication.quit()
            #app = QtWidgets.QApplication(sys.argv)
            #dialog = QtWidgets.QDialog()
            #self.ui = MainApp()
            #self.ui.panel(dialog)
            #dialog.show()
            #sys.exit(app.exec_())


def sign_up():
    _translate = QtCore.QCoreApplication.translate
    ui.label.setText(_translate("Dialog", "sign up in Form"))
    if(ui.count==-2):
        ui.count=-1
        return
    same=search_user(ui.lineEdit.text())
    if(same==True):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("the user is exist")
        error_dialog.exec_()
        ui.lineEdit.setText("")
        ui.lineEdit_2.setText("")
    elif(ui.lineEdit_2.text()==""):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("your password cant be empty")
        error_dialog.exec_()
        uilineEdit.setText("")
        ui.lineEdit_2.setText("")
    else:
        create_user(ui.lineEdit.text(), ui.lineEdit_2.text())
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setText("your signup its success please login")
        error_dialog.exec_()
        ui.lineEdit.setText("")
        ui.lineEdit_2.setText("")




#if __name__ == "__main__":
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QMainWindow() #.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

sys.exit(app.exec_())
