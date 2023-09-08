from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    def dfs(n,computer):
        deq = deque()
        deq.append(computer)
        while deq:
            computer = deq.popleft()
            visited[computer]=1
            for network in range(n):
                if computer!=network and computers[computer][network]==1 and visited[network]==0:
                    deq.append(network)
                    
    for computer in range(n):
        if visited[computer]==0:
            visited[computer]=1
            dfs(n, computer)
            answer += 1
    
    return answer
# dfs를 solution안쪽에 넣으면 computers나 visited 파라미터를 넣어줄 필요가 없음! 새로운 사실
