from collections import deque
def solution(maps):
    # 상하좌우
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    deq = deque()
    deq.append((0,0))
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 구간 범위 체크
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                # maps[nx][ny]가 1이라면 아직 가지 않은 곳
                if maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y]+1
                    deq.append((nx,ny))
                    
    if maps[-1][-1]==1:
        return -1
    else:
        return maps[-1][-1]
        
    
    
    
    
    
    
    
    