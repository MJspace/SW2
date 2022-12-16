import time #라이브러리
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target): #(재귀적 탐색)
    while (l<=u):
        middle=int((l+u)//2)
        if L[middle]==target:
            return middle
            break
        elif L[middle]<target:
            return recbinsearch(L,middle+1,u,target)
        else:
            return recbinsearch(L,l,middle-1,target)
    return -1 #구간내에 찾고자 하는 target값이 아예 없을때


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]
#print(type(targets[0]))=int

ts = time.time()

# binary search - recursive
cnt = 0
for target in targets: #targets에 target이 있을 때까지 돌림 / targets의 각 인덱스 값을 하나씩 L리스트에 있는지 비교하는 것, 즉 targets 모두가 target 대상임
    idx = recbinsearch(numbers, 0, len(numbers), target) #numbers는 리스트
    if idx == -1:
        cnt += 1 #못 찾은 횟수를 계산
ts = time.time() - ts #총 걸린 시간에서 시작했을 때 걸린 시간을 빼줌->걸린 시간 만을 계산
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))