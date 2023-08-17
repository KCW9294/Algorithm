from collections import deque
N,M = map(int,input().split())
road = [list(map(int,input())) for _ in range(N)]

deq = deque()
deq.append((0,0))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while deq:
    x,y = deq.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<N and 0<=ny<M and road[nx][ny]==1:
            deq.append((nx,ny))
            road[nx][ny] = road[x][y] + 1

print(road[N-1][M-1])