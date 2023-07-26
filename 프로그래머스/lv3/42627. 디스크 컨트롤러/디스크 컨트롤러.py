import heapq
def solution(jobs):
    n_jobs = len(jobs)
    answer, start, current, num = 0,-1,0,0
    heap = []
    
    while num < n_jobs:
        for job in jobs:
            if start < job[0] <= current:
                heapq.heappush(heap,(job[1],job[0]))
            
        if heap:
            d, s = heapq.heappop(heap)
            start = current
            current += d
            answer += (current - s)
            num += 1
        else:
            current += 1
            
    return int(answer/n_jobs)