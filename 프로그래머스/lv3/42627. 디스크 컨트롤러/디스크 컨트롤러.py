import heapq
def solution(jobs):
    n_jobs = len(jobs)
    answer, start, current, num = 0,-1,0,0 # 시작지점, 현재시점 변수 정의
    heap = [] # heap을 사용하여 작업의 소요시간을 기준으로 오름차순 정렬해야함
    
    while num < n_jobs:
        for job in jobs:
            if start < job[0] <= current: # 시작지점보다 크고 현재시점보다 작은 작업들을 골라줌
                heapq.heappush(heap,(job[1],job[0])) # 작업의 소요시간 기준으로 오름차순 정렬하기 위해 job[1]을 먼저 넣어줌
            
        if heap:
            d, s = heapq.heappop(heap)
            start = current # 시작지점을 현재 시점으로 갱신
            current += d # 현재시점에 작업 소요시간을 더해줌
            answer += (current - s) # 현재시점 - 작업이 요청되는 시점을 해줘야 대기한 시간만큼 빼줄 수 있음
            num += 1
        else:
            current += 1 # 작업이 없는 경우 현재시점을 늘려줘야함
            
    return int(answer/n_jobs)
