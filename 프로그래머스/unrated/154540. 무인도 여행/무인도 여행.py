import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def solution(maps):
    answer = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    node = [[0]*len(maps[0]) for _ in range(len(maps))]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def dfs(i,j):
        temp.append(int(maps[i][j]))
        visited[i][j]=True
        for k in range(4):
            if 0<=i+dx[k]<len(maps) and 0<=j+dy[k]<len(maps[0]):
                if visited[i+dx[k]][j+dy[k]]==False and maps[i+dx[k]][j+dy[k]]!='X':
                    dfs(i+dx[k],j+dy[k])
                    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            temp = []
            if visited[i][j]==False and maps[i][j]!='X':
                dfs(i,j)
                answer.append(sum(temp))
                
    if not answer:
        return [-1]
                
    answer.sort()
    return answer