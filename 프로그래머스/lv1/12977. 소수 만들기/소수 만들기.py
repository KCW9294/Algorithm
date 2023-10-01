from itertools import permutations,combinations
def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        temp = sum(i)
        cnt = 0
        for k in range(2,temp):
            if temp%k==0:
                cnt += 1
                break
        if cnt==0:     
            answer += 1
    return answer