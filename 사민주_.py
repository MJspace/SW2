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


#인덱스 에러 (마저 다 기록하지 않았을 때)
#변수 에러(스트링 자리에 인트 대입했을 때)
#for 문 아닌 곳에 break 넣은 것 지움 -> 연결 끊기지 않고 다시 그 상태에서 입력 받게 하기 위함 (add 부분)
#inc 부분 추가 점수 제한(100점 이하여야 함)
