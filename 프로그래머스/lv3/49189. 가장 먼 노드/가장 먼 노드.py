from collections import deque
def solution(n, edge):
    answer = [0]*(n+1)
    visited = [False]*(n+1)
    temp = []
    node = [[] for _ in range(n+1)]

    def bfs(start):
        deq = deque([start])
        visited[start] = True
        while deq:
            start = deq.popleft()
            for i in node[start]:
                if visited[i] == False:
                    visited[i] = True
                    answer[i] = answer[start]+1
                    deq.append(i)
    
    for x,y in edge:
        node[x].append(y)
        node[y].append(x)
    
    for i in range(len(node)):
        if visited[i]==False:
            bfs(i)
                    
    return answer.count(max(answer))
