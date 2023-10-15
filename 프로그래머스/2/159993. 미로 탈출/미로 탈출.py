from collections import deque

def bfs(start, end, maps):
	# 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1] 
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    que = deque()
    out = False
    
    # 초깃값 설정
    for i in range(len(maps)):
        for j in range(len(maps[0])):
        	# 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:      
                que.append((i, j, 0))    
                visited[i][j] = True
                flag = True; break 
        if out: break
                
    while que:
        x, y, cost = que.popleft()
        
        if maps[x][y] == end:
            return cost
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<= nx <len(maps) and 0<= ny <len(maps[0]) and maps[nx][ny] !='X' and visited[nx][ny]==False:
                que.append((nx, ny, cost+1))
                visited[nx][ny] = True
                    
    return -1	# 탈출할 수 없다면
        
def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    
    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
   	# 둘중 하나라도 -1 이면 탈출할 수 없음
    return -1