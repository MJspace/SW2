dbfilename = 'test3_2.dat' #dbfilename이라는 변수에 'test3_2.dat'이라는 파일의 이름을 문자열로 저장

def readScoreDB(): #readScoreDB라는 함수 정의 (읽기)
    try:
        fH = open(dbfilename) #dbfilename에 저장했던 파일을 열음
    except FileNotFoundError as e: #예외처리) file을 찾지 못해서 에러가 발생, FileNotFoundError를 변수 e에 저장
        print("New DB: ", dbfilename) #예외 발생시 문자열 출력
        return []
    else: #오류가 발생하지 않을 경우
        print("Open DB: ", dbfilename) #오류 발생하지 않을 시 파일 열겠다는 문자열 출력

    scdb = [] #scdb라는 빈 리스트 생성
    for line in fH: #파일의 라인을 하나씩 읽음
        dat = line.strip() #라인의 개행문자 제거해서 변수에 저장
        person = dat.split(",") #,단위로 라인을 나눠서 변수에 저장
        record = {} #빈 딕셔너리를 생성
        for attr in person: #person에 저장된 데이터를 attr로 저장
            kv = attr.split(":") #:단위로 attr을 나누고 kv에 저장
            record[kv[0]] = kv[1] #kv 인덱스 0의 값을 키로 변환후 그 값을 kv 인덱스 1의 값으로 저장
        scdb += [record] #scdb에 리스트로 변환된 record를 넣음
    fH.close() #파일을 닫음
    return scdb #scdb 리스트를 리턴


# write the data into person db
def writeScoreDB(scdb): #writeScoreDB라는 함수 정의(쓰기)
    fH = open(dbfilename, 'w') #파일을 쓰기모드로 염
    for p in scdb: #변수 p에 scdb의 리스트를 받아옴
        pinfo = [] #빈 리스트를 생성
        for attr in p: #변수 attr에 p의 데이터를 받아옴
            pinfo += [attr + ":" + p[attr]] #pinfo에 키 : 값 저장
        line = ','.join(pinfo) #pinfo를 ,단위를 기준으로 문자열로 반환
        fH.write(line + '\n') #파일 쓰기
    fH.close() #파일 닫기


def doScoreDB(scdb): #doScoreDB라는 함수 정의
    while(True):
        inputstr = (input("Score DB > ")) #inputstr에 문자열 입력받음
        if inputstr == "": continue #만약 inputstr 값이 빈값이면 컨티뉴
        parse = inputstr.split(" ") #inputstr을 공백 기준으로 나눠 저장
        if parse[0] == 'add': #만약 parse 인덱스 0의 값이 add라면
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]} #record딕셔너리 새로 생성
            scdb += [record] #scdb에 리스트로 변환한 record를 추가 저장
        elif parse[0] == 'del': #만약 parse 인덱스 0의 값이 del면
            for p in scdb: #scdb의 데이터를 p에 저장
                if p['Name'] == parse[1]: #만약 p의 키(name)가 parse의 인덱스 1의 값과 같은 경우
                    scdb.remove(p)    #scdb의 p를 지움
                    break #끝냄
        elif parse[0] == 'show': #만약 parse 인덱스 0의 값이 show면
            sortKey ='Name' if len(parse) == 1 else parse[1]# parse의 길이가 1이면 sortKey를 출력하고 아니면 parse 인덱스1 출력
            showScoreDB(scdb, sortKey) #함수 실행
        elif parse[0] == 'quit': #만약 parse 인덱스 0 값이 quit일 경우
            break #끝냄
        else: #다른경우
            print("Invalid command: " + parse[0]) #문자열 및 parse의 0인덱스 출력


def showScoreDB(scdb, keyname): #showScoreDB 함수 정의
    for p in sorted(scdb, key=lambda person: person[keyname]): # 파일 내용을 k로 정렬
        for attr in sorted(p): #정렬한 p 값을 attr에 저장
            print(attr + "=" + p[attr], end=' ') #결과값을 출력
        print() #공백출력

#실행
scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
