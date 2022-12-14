import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    print(scdb)
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                scdb += [record]
            except IndexError as e:
                print(e)
        elif parse[0] == 'del':
            try:
                for p in scdb[::-1]:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError as e:
                print(e)
                break
            except KeyError as e:
                print(e)
                break
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except IndexError as e:
                print(e)
                break
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        print(p)
                        break
                    except IndexError as e:
                        print(e)
                        break
        elif parse[0] == 'inc':
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        p["Score"] = int(parse[2]) + int(p['Score'])
                        print(int(p['Score']))
                        break
                    except IndexError as e:
                        print(e)
                        break

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(str(attr) + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)


#????????? ?????? (?????? ??? ???????????? ????????? ???)
#?????? ??????(????????? ????????? ?????? ???????????? ???)
#for ??? ?????? ?????? break ?????? ??? ?????? -> ?????? ????????? ?????? ?????? ??? ???????????? ?????? ?????? ?????? ?????? (add ??????)
#inc ?????? ?????? ?????? ??????(100??? ???????????? ???)
