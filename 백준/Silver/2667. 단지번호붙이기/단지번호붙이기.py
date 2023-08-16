N = int(input())
node = [list(map(int,input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
answer = []

nx = [0,0,1,-1]
ny = [1,-1,0,0]

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return 0
    if visited[x][y]==True or node[x][y]==0:
        return 0

    visited[x][y]=True
    temp = 1
    for k in range(4):
        temp += dfs(x+nx[k],y+ny[k])

    return temp

for i in range(N):
    for j in range(N):
        if node[i][j]!=0 and visited[i][j]==False:
            answer.append(dfs(i,j))
            
answer.sort()            
print(len(answer))
for i in answer:
    print(i)