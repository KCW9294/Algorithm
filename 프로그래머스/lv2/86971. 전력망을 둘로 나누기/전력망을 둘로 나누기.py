from collections import deque
def solution(n, wires):
    res = n
    graph = [[] for i in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visited = [0]*(n+1)
        cnt=1
        q = deque([start])
        visited[start] = 1
        while q:
            s = q.pop()
            for i in graph[s]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt    
    
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(bfs(a)-bfs(b)),res)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return res
        
                