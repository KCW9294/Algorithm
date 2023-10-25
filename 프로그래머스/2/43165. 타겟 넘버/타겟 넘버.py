from collections import deque
def solution(numbers, target):
    answer = 0
    deq = deque()
    deq.append((numbers[0],0))
    deq.append((-numbers[0],0))
    while deq:
        num, idx = deq.popleft()
        if idx == len(numbers)-1:
            if num == target:
                answer += 1
        else:
            idx += 1
            deq.append((num+numbers[idx],idx))
            deq.append((num-numbers[idx],idx))
    return answer