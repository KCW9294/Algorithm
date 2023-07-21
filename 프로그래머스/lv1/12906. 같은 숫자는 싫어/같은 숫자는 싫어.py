from collections import deque
def solution(arr):
    deq = deque(arr)
    answer = []
    for i in range(len(deq)):
        unique = deq.popleft()
        if i==0:
            answer.append(unique)
        else:
            if unique != answer[-1]:
                answer.append(unique)
    return answer