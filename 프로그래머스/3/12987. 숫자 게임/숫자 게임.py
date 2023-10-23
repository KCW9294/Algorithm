import heapq
def solution(A, B):
    answer = 0
    A.sort()
    heapq.heapify(B)
    i = 0
    while B:
        if A[i] < B[0]:
            answer += 1
            heapq.heappop(B)
            i += 1
        else:
            heapq.heappop(B)
            
    return answer