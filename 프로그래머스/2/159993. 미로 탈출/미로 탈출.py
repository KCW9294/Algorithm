from collections import deque

def bfs(start, end, maps):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    n = len(maps)
    m = len(maps[0])
    q = deque()
    out = False
    visited = [[False]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]==start:
                q.append((i,j,0))
                visited[i][j] = True
                out = True
                break
        if out:
            break
    
    while q:
        x,y,cost = q.popleft()
        if maps[x][y]==end:
            return cost
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and maps[nx][ny]!='X':
                visited[nx][ny]=True
                q.append((nx,ny,cost+1))
    
    return -1
                
def solution(maps):
    result1 = bfs('S','L',maps)
    result2 = bfs('L','E',maps)
    
    if result1!=-1 and result2!=-1:
        return result1+result2
    else:
        return -1
