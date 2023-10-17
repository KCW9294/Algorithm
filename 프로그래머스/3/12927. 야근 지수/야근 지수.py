import heapq
def solution(n, works):
    answer = 0
    if sum(works)-n<=0:
        return 0
    else:
        for i in range(len(works)):
            works[i] *= -1
        heapq.heapify(works)
        
        for i in range(n):
            temp = heapq.heappop(works)
            heapq.heappush(works,temp+1)
            
        for i in works:
            answer += (i*(-1))**2
            
    return answer