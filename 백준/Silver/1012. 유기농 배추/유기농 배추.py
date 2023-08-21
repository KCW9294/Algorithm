import sys
sys.setrecursionlimit(10000)

T = int(input())
test_case = [0]*T
answer = [0]*T
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for t in range(T):
    M,N,K = map(int,input().split())
    lst = [[0]*N for _ in range(M)]
    for i in range(K):
        x,y = map(int,input().split())
        lst[x][y]=1
    visited = [[False]*N for _ in range(M)]
    
    def dfs(x,y):
        visited[x][y]=True
        for k in range(4):
            if 0<=x+dx[k]<M and 0<=y+dy[k]<N:
                if visited[x+dx[k]][y+dy[k]]==False and lst[x+dx[k]][y+dy[k]]==1:
                    dfs(x+dx[k],y+dy[k])
            
    for i in range(M):
        for j in range(N):
            if visited[i][j]==False and lst[i][j]==1:
                visited[i][j]=True
                dfs(i,j)
                answer[t]+=1
         
for i in answer:
    print(i)
