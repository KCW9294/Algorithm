from collections import deque
def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        
        if len(scoville) <=1:
            break
        scoville = list(scoville)
        scoville.sort()
        scoville = deque(scoville)
        min_1 = scoville.popleft()
        min_2 = scoville.popleft()
        scoville.append(min_1 + min_2*2)
        answer += 1
    if len(scoville)==0 or min(scoville)<K:
        answer = -1
    
    return answer
