def solution(lst):
    # dic=dict.fromkeys(lst)
    # print(dic)
    counter={}
    for value in lst:
        if value in counter:
            counter[value]+=1
        else:
            counter[value]=1
    a = [k for k, v in counter.items() if max(counter.values()) == v and v>1]
    return a

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]