from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for line in edge:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    answer = [1]*(n+1)
    deq = deque()
    deq.append(1)
    visited = [0]*(n+1)
    visited[1] = 1
    
    while deq:
        node = deq.popleft()
        for i in graph[node]:
            if visited[i]==0:
                deq.append(i)
                answer[i] = answer[node]+1
                visited[i] = 1

    return answer.count(max(answer))
