import sys
sys.setrecursionlimit(10000)

N,M=map(int,input().split())
node = [[] for _ in range(N+1)]
answer = 0

for i in range(M):
    x,y = map(int,input().split())
    node[x].append(y)
    node[y].append(x)

visited = [False] * (N+1)    

def dfs(start):
    visited[start]=True
    for i in node[start]:
        if visited[i] == False:
            dfs(i)

for i in range(1,N+1):
    if visited[i]==False:
        dfs(i)
        answer += 1
        
print(answer)