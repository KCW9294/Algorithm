from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for computer in range(n):
        if visited[computer]==0:
            visited[computer]=1
            dfs(n, computers, computer, visited)
            answer += 1
    
    return answer
            
            
def dfs(n, computers, computer, visited):
    deq = deque()
    deq.append(computer)
    while deq:
        computer = deq.popleft()
        visited[computer]=1
        for network in range(n):
            if computer!=network and computers[computer][network]==1 and visited[network]==0:
                deq.append(network)
