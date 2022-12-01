from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.namedb = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.StudentList = QtWidgets.QTextEdit(self.centralwidget)  # 학생명단 출력창
        self.StudentList.setReadOnly(True)  # 글자 입력 못하게 바꿈, 출력만 하게
        self.StudentList.setGeometry(QtCore.QRect(10, 310, 401, 141))
        self.StudentList.setObjectName("StudentList")

        self.Input = QtWidgets.QLineEdit(self.centralwidget)  # 학생 이름 추가 입력창
        self.Input.setGeometry(QtCore.QRect(10, 270, 191, 20))  # x축, y축 -> 위치/ 가로, 세로
        self.Input.setObjectName("Input")

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(210, 270, 41, 23))
        self.addButton.setObjectName("addButton")  # add 인원
        self.addButton.clicked.connect(self.addbuttonClicked)

        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(255, 270, 41, 23))
        self.delButton.setObjectName("delButton")  # del 해당이름
        self.delButton.clicked.connect(self.delbuttonClicked)

        # self.show()

        #이 grid 뭔지 모르겠음
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 110, 401, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")  #

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.Student6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student6.setObjectName("Student6")
        self.gridLayout.addWidget(self.Student6, 1, 1, 1, 1)
        self.Student2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student2.setObjectName("Student2")
        self.gridLayout.addWidget(self.Student2, 0, 1, 1, 1)
        self.Student8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student8.setObjectName("Student8")
        self.gridLayout.addWidget(self.Student8, 1, 3, 1, 1)
        self.Student4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student4.setObjectName("Student4")
        self.gridLayout.addWidget(self.Student4, 0, 3, 1, 1)
        self.Student7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student7.setObjectName("Student7")
        self.gridLayout.addWidget(self.Student7, 1, 2, 1, 1)
        self.Student3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student3.setObjectName("Student3")
        self.gridLayout.addWidget(self.Student3, 0, 2, 1, 1)
        self.Student5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student5.setObjectName("Student5")
        self.gridLayout.addWidget(self.Student5, 1, 0, 1, 1)
        self.Student1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student1.setObjectName("Student1")
        self.gridLayout.addWidget(self.Student1, 0, 0, 1, 1)
        self.Student_NULL = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student_NULL.setObjectName("Student_NULL")
        self.gridLayout.addWidget(self.Student_NULL, 2, 3, 1, 1)

        self.StartButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.StartButton.setObjectName("StartButton")
        self.gridLayout.addWidget(self.StartButton, 3, 0, 1, 1)
        self.StartButton.clicked.connect(self.startbuttonClicked)
        self.SurrenderButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SurrenderButton.setObjectName("SurrenderButton")
        self.gridLayout.addWidget(self.SurrenderButton, 3, 1, 1, 1)

        self.TeacherSays = QtWidgets.QTextEdit(self.centralwidget)
        self.TeacherSays.setReadOnly(True) #글자 입력 못하게 바꿈, 출력만 하게
        self.TeacherSays.setGeometry(QtCore.QRect(129, 30, 161, 51))  # 선생님 호명
        self.TeacherSays.setObjectName("TeacherSays")

        self.Left_Time = QtWidgets.QProgressBar(self.centralwidget)
        self.Left_Time.setGeometry(QtCore.QRect(300, 40, 111, 23))
        self.Left_Time.setProperty("value", 50)
        self.Left_Time.setObjectName("Left_Time")  # 배터리=남은시간

        self.Score_label = QtWidgets.QLabel(self.centralwidget)
        self.Score_label.setGeometry(QtCore.QRect(320, 270, 31, 21))
        self.Score_label.setObjectName("Score_label")

        self.Score = QtWidgets.QLabel(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(360, 270, 51, 20))
        self.Score.setObjectName("Score")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #score 비교시 Score_label ==5?이런식? 이거 어케함
    def retranslateUi(self, MainWindow):  # 기본 숫자 설정
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Student6.setText(_translate("MainWindow", "6"))
        self.Student2.setText(_translate("MainWindow", "2"))
        self.Student8.setText(_translate("MainWindow", "8"))
        self.Student4.setText(_translate("MainWindow", "4"))
        self.Student7.setText(_translate("MainWindow", "7"))
        self.Student3.setText(_translate("MainWindow", "3"))
        self.Student5.setText(_translate("MainWindow", "5"))
        self.Student1.setText(_translate("MainWindow", "1"))
        self.Student_NULL.setText(_translate("MainWindow", "X")) #호명한 학생이 없는 경우
        self.StartButton.setText(_translate("MainWindow", "Game Start!"))
        self.SurrenderButton.setText(_translate("MainWindow", "Surrender"))
        self.Score_label.setText(_translate("MainWindow", "Score:"))
        self.Score.setText(_translate("MainWindow", "0"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.delButton.setText(_translate("MainWindow", "Del"))

    def showStudentList(self):
        self.StudentList.clear()
        sum=""
        for i in self.namedb:
            sum = sum + " " + i
        self.StudentList.append(sum)

    def addbuttonClicked(self):
        text = self.Input.text()
        # text_ = text.split() -> 이름 여러개 들어왔을 때
        self.namedb.append(text)
        # self.StudentList.setText(text)
        self.showStudentList()
        self.Input.clear()

    def delbuttonClicked(self):
        for i in self.namedb:
            if i == self.Input.text():
                self.namedb.remove(i)
        self.showStudentList()

    def showTeacherSays(self):
        self.TeacherSays.clear()
        name = random.choice(self.namedb)
        self.TeacherSays.append(name)
        self.TeacherSays.setAlignment(Qt.AlignCenter)

    def startbuttonClicked(self):
        self.showTeacherSays()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
