import pickle #package import

dbfilename = 'test3_4.dat' #파일 이름 설정

def readScoreDB():
    try: #파일 오픈 실패를 위한 try-catch문
        fH = open(dbfilename, 'rb') #원래 잇던 db 리턴
    except FileNotFoundError:
        print("New DB: ", dbfilename) #새로 만들었단걸 알려주기 위한 출력문
        return [] #빈 리스트 리턴

    scdb = []
    try:
        scdb =  pickle.load(fH) #rb로 오픈한 파일 객체화 오픈 시도
        for p in scdb: #scdb 안에 있는 인자 하나하나씩 읽기
            #print(p)
            p['Age'] = int(p['Age']) #Age int로 형식 변환
            p['Score'] = int(p['Score']) #Sore int로 형식 변환
            #print(type(p['Name']),type(p['Age']),type(p['Score']))
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb #dbfilename 파일을 리턴


# write the data into person db
def writeScoreDB(scdb): #저장
    fH = open(dbfilename, 'wb') #쓰기(이진) 형식으로 오픈
    pickle.dump(scdb, fH) #fh파일 안에 scdb(객체)를 이진형식으로 저장
    fH.close() #파일 닫기


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > ")) #명령문을 입력받아 저장
        if inputstr == "": continue #다시 시도
        parse = inputstr.split(" ") #공백 기준으로 split
        if parse[0] == 'add': #첫번째 인덱스가 가르키는 명령어가 add 일 때 실행
            try:
                parse[2] = int(parse[2]) #입력받은 값(Age) int로 변경
                parse[3] = int (parse[3]) #입력받은 값(Score) int로 변경
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]} #dictionary 형태
                scdb += [record] #scdb 안에 record(dict형태) 저장
            except IndexError as e:
                print(e)
            except ValueError as d:
                print(d)
        elif parse[0] == 'del':
            try:
                for p in scdb[::-1]:
                    if p['Name'] == parse[1] :
                        scdb.remove(p)
            except IndexError as e:
                print(e)
            except ValueError as d:
                print(d)
        elif parse[0] == 'show': # show라는 명령어
            sortKey ='Name' if len(parse) == 1 else parse[1] #따로 정의를
            showScoreDB(scdb, sortKey) #show  수행
        elif parse[0] == 'find': #이름 기준으로 탐색
            for p in scdb: #scdb 안에 있는 인자 하나하나씩 읽기
                try:
                    if p['Name'] == parse[1]: # p안에 Name이라는 key의 value가 parse[1]과 일치한다면 출력
                        print("Name: %s, Age %d, Score %d" %(p['Name'],p['Age'],p['Score']) )
                except IndexError as e:
                    print(e)
                    break
                except ValueError as d:
                    print(d)
                    break
        elif parse[0] == 'inc': #점수 추가
            for p in scdb: #scdb 안에 있는 인자 하나하나씩 읽기
                if p['Name'] == parse[1]: # p안에 Name이라는 key의 value가 parse[1]과 일치한다면 출력
                    try:
                        p['Score'] = p['Score'] + int(parse[2]) # 값 추가
                        if p['Score'] > 100 :
                            p['Score']-=int(parse[2])
                            print("추가 점수는 100점 이하여야 합니다.")
                        break
                    except IndexError as e:
                        print(e)
                        break
                    except ValueError as d:
                        print(d)
                        break
        elif parse[0] == 'quit': #명령 종료
            break
        else:
            print("Invalid command: " + parse[0]) #잘못된 명령문 입력시


def showScoreDB(scdb, keyname): #함수
    for p in sorted(scdb, key=lambda person: person[keyname]): #scdb 정렬, 정렬기준을 keyname으로 정렬한다.
        for attr in sorted(p): #attr
            print(attr + "=" + str(p[attr]), end=' ') #정렬된거를 하나씩 출력
        print() #띄어쓰기 출력


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)