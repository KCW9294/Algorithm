from collections import deque
M,N = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
max_num, answer = 0, 0
deq = deque()
nx = [1,-1,0,0]
ny = [0,0,1,-1]
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            deq.append((i,j))

while deq:
    x,y = deq.popleft()
    for i in range(4):
        if 0<=x+nx[i]<N and 0<=y+ny[i]<M:
            if graph[x+nx[i]][y+ny[i]]==0:
                graph[x+nx[i]][y+ny[i]]=graph[x][y]+1
                deq.append((x+nx[i],y+ny[i]))

for i in graph:
    if 0 in i:
        answer = -1
        break
    else:
        if max(i)>max_num:
            max_num = max(i)
if answer == 0:
    print(max_num-1)
else:
    print(answer)
