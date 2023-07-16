from itertools import *
def solution(numbers):
    all = []
    answer = 0
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            all.append(int(''.join(j)))
    all = list(set(all))
    for i in all:
        cnt=0
        if i == 1 or i == 0:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                cnt+=1
        if cnt==0:
            answer += 1
    return answer