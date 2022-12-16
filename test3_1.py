import sys
fname = input("Enter data file name: ") #fname에 파일이름을 입력 받는다.
try:
    fH = open(fname) #fname에 저장된 파일을 열음
except FileNotFoundError as e:
    print("No such file: " + fname) #fname에서 입력받은 파일을 찾지 못할 경우 그러한 파일이 없다는 문구를 출력
    sys.exit()

wordcount = {}
for line in fH:
    words = line.split() #파일에서 라인을 읽고 그 라인들을 공백으로 분리함

    for word in words: #공백으로 분리한 라인의 단어를 읽음
        if word in wordcount:
            wordcount[word] += 1 #만약 wordcount에 단어가 발견되면 개수를 증가시켜 처음 출현한 단어인지 파악
        else:
            wordcount[word] = 1 #만약 단어가 발견되지 않으면 단어출현 횟수를 1로 고정

fH.close() #파일을 닫음

for word in wordcount: #결과를 출력
    print(word, ":", wordcount[word])
