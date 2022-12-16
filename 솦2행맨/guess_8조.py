#집합은 순서가 없음
#secretword랑 guessedChars 순서 제대로 안하면 _의 수가 나중에 바뀜(뒤죽박죽)->무엇을 찾고자 하는지 목적 변수가 중요
class Guess:

    def __init__(self, word):
        self.currentStatus = "_" * len(word)
        self.secretWord = word #찾아야 하는 단어
        self.guessedChars = set()
        self.numTries = 0 #실패한 횟수

    def display(self): #Current값과 Tries 값 출력
        print("Current: " + self.currentStatus)
        print("Tries: %d" %self.numTries)


    def guess(self, character):
        self.guessedChars.add(character) #초기화 된 집합 guessedChars에 사용자가 입력한 character 원소 넣어줌
        if character in self.secretWord: #사용자가 입력한 게 word 안에 있다면
            find = ""
            for i in self.secretWord: #secretWord 글자를 하나씩 읽음 -> secretWord 대신 guessedChars로 먼저 비교하면 find가 뒤죽박죽-> 게스드는 집합이라 순서가 없기 때문, 그래서 순서가 제대로인 워드로 해서 순차적으로 find에 추가
                if i in self.guessedChars: #character 그 자체랑 비교하는 게 아닌! character들의 집합인 guessedChars와 비교! 그래야 guessedChars 만든 의미있음 -> i가 사용자가 입력한 글자의 조합에 있다면 find 문자열에 추가
                    find += i
                else:
                    find += "_" #없을 경우 _ 추가
            self.currentStatus = find #find 더한 거로 저장
        else: #사용자 입력 값이 word에 존재 하지 않을 경우
            self.numTries += 1 #실패 횟수 증가시킴

        if self.currentStatus == self.secretWord:
            return True  #True, False 통해 game에서 성공 여부 나타내기 위해
        else:
            return False