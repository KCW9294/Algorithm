from collections import deque

N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)
            
def bfs(start):
    deq = deque([start])
    visited[start] = True
    while deq:
        start = deq.popleft()
        print(start, end=" ")
        for i in graph[start]:
            if visited[i] == False:
                visited[i] = True
                deq.append(i)
            

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)