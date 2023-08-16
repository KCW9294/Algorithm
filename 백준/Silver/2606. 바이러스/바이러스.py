from collections import deque

N = int(input())
M = int(input())
node = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

    
visited = [False] * (N+1)
def bfs(start):
    q = deque([start])
    answer = 0
    while q:
        start = q.popleft()
        visited[start] = True
        for i in node[start]:
            if visited[i]==False:
                q.append(i)
                visited[i] = True
                answer += 1
    print(answer)
    
bfs(1)
