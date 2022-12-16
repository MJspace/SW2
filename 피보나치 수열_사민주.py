#피보나치 재귀적 함수
import time

def fibo(n): #재귀적 구현
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n): #반복적 구현
    a=1
    b=1
    if n<= 1: #0번째와 1번째 항
        return n
    else:
        for i in range(n-2): #3번째 항부터만 구하면 됨을 명심! /3부터 반복문 실행됨
            num=b
            b+=a #b가 새로 구하고자 하는 항 (전항의 두 합)
            a=num #num을 b로 바꿀 수 없는 이유-> 그 전줄에서 b가 새롭게 갱신되어 초기 b값이 아닌 갱신된 b값이 더해지기 때문
        return b #n=2일때는 그냥 b의 값 도출


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))


