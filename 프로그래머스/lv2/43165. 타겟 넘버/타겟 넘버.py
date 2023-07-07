from collections import deque
def solution(numbers, target):
    answer = 0
    deq = deque()
    deq.append([numbers[0],0])
    deq.append([-1*numbers[0],0])
    
    while deq:
        num, idx = deq.popleft()
        idx += 1
        if idx<len(numbers):
            deq.append([num+numbers[idx],idx])
            deq.append([num-numbers[idx],idx])
        else:
            if num == target:
                answer += 1

    return answer