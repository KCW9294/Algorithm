from collections import deque
def solution(n, computers):
    answer = 0
    deq = deque()
    visited = [0]*n
    deq.append(0)
    for i in range(n):
        if visited[i]==0:
            deq.append(i)
            while deq:
                node = deq.popleft()
                visited[node] = 1
                for k in range(len(computers[node])):
                    if visited[k]==0 and computers[node][k]==1:
                        deq.append(k)
        else:
            continue
        answer += 1
    
    return answer