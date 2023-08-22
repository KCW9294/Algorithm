from collections import deque
def solution(queue1, queue2):
    answer = -2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt = 0
    for i in range(len(queue1)*4):
        if sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        elif sum1 < sum2:
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp
        cnt += 1
        
    return -1