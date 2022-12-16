# def solution(num):
#     a=str(num)
#     b=0
#     for i in a:
#         b+=int(i)
#     return b
# print(solution(5923))
# print(solution(200))
# print(solution(1234567890))
# print(solution(2364759387))

data=input("Enter list of numbers: ") #str
numbers=data.split() #list(str) 공백기준으로 정렬
print(numbers)
numbers=[int(i) for i in numbers] #[str->int]
print(numbers)
def RecursiveArraySum(nbrs,k):
    if k==0: #k=o인 경우 즉 k=0이 될때까지 돌림
        return nbrs[0]
    return RecursiveArraySum(nbrs, k-1) + nbrs[k]#나머지 경우(재귀함수)
print("Recursive Array Sum:", RecursiveArraySum(numbers,len(numbers)-1))
