from collections import deque
def solution(maps):
    answer = 0
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        deq = deque()
        deq.append((x,y))
        
        while deq:
            x, y = deq.popleft()
            
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                if nx<0 or nx>=len(maps) or ny<0 or ny >=len(maps[0]):
                    continue
                if maps[nx][ny]==0:
                    continue
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    deq.append((nx,ny))
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0,0)
    if answer == 1:
        answer = -1
    else:
        answer = maps[len(maps)-1][len(maps[0])-1]
    return answer