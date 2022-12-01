import random

class DataBase:
    def __init__(self):
        self.namedb = []
        self.scoredb = 0
        self.teachersays = []
        self.currentstage = -1
        self.pickStudent=[]

    def getstudentlist(self):
        studentlist = ""
        for i in self.namedb:
            studentlist = studentlist + " " + i
        return studentlist

    def addstudent(self, studentname):
        self.namedb.append(studentname)

    def deletestudent(self, studentname):
        for i in self.namedb:
            if i == studentname:
                self.namedb.remove(i)

    #namedb명단에서 랜덤으로 8명 뽑음
    def pickStudent(self):
        self.pickStudent = random.sample(self.namedb, 8)

    def setteachersays(self):
        self.teachersays.append(random.sample(self.pickStudent,1))
        self.currentstage += 1
        return self.teachersays[self.currentstage]




