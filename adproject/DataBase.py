import random


# namedb명단에서 랜덤으로 num명 뽑음
def pickStudent(list, num):
    pickStudent = random.sample(list, num)
    return pickStudent


class DataBase:
    def __init__(self):
        self.namedb = []
        self.scoredb = 0
        self.teachersays = []
        self.student_button = []
        self.currentstage = 0

    def setScore(self):
        self.scoredb = 0
        self.currentstage = 0

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

    def setteachersays(self):
        self.teachersays = pickStudent(self.namedb, 5)
        self.currentstage = 0

    def getTeachersays(self):
        name = self.teachersays[self.currentstage]

        return name

    def setStudent_button(self):
        self.student_button = pickStudent(self.namedb, 8)

    def getStudent_button(self):
        return self.student_button

    def compareData(self, num):
        if (num == 8):
            if (self.teachersays[self.currentstage] not in self.student_button):
                self.scoredb += 1
        elif num >= 0:
            if (self.teachersays[self.currentstage] == self.student_button[num]):
                self.scoredb += 1
        if (self.currentstage != 4):
            self.currentstage += 1
            return 1
        else:
            return 0

    def getScore(self):
        return self.scoredb

    def getcurrentstage(self):
        return self.currentstage



