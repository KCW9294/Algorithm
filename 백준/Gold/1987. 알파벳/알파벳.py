import sys
input = sys.stdin.readline

R,C = map(int,input().split())
matrix = [list(input().strip()) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0
alpha_set = [True] * 26
alpha_set[ord(matrix[0][0]) - 65] = False

def dfs(start,cnt):
    global result
    x,y = start
    if cnt>result:
        result = cnt
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and alpha_set[ord(matrix[nx][ny]) - 65]:
            alpha_set[ord(matrix[nx][ny]) - 65] = False
            dfs((nx,ny),cnt+1)
            alpha_set[ord(matrix[nx][ny]) - 65] = True
            
dfs((0,0),1)
print(result)
