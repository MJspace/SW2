import random

# namedb명단에서 랜덤으로 8명 뽑음
def pickStudent(num):
    pickStudent = random.sample(num, 8)
    return pickStudent

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


    def setteachersays(self):
        picked = pickStudent(self.namedb)
        a = random.choice(picked)
        while a not in self.teachersays:
            self.teachersays.append(a)
        self.currentstage += 1
        return self.teachersays[self.currentstage]
        # if a not in self.teachersays:
        #     self.teachersays.append(a)
        # else:
        #
        # self.currentstage += 1
        # return self.teachersays[self.currentstage]






