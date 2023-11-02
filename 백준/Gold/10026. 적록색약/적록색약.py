import sys
sys.setrecursionlimit(10**6)

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[False]*N for _ in range(N)]

def dfs(x,y,color):
    visited[x][y]=True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and color==matrix[nx][ny]:
            dfs(nx,ny,color)

not_sick = 0
sick = 0
            
for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            color = matrix[i][j]
            dfs(i,j,color)
            not_sick += 1
            
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        matrix[i][j] = matrix[i][j].replace('R','G')

for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            color = matrix[i][j]
            dfs(i,j,color)
            sick += 1
            
print(not_sick,sick)