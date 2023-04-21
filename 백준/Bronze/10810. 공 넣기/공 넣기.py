N,M = map(int, input().split())
lst = [0 for i in range(N)]
t_d = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    for k in range(t_d[i][0],t_d[i][1]+1):
            lst[k-1]=t_d[i][2]
for i in range(len(lst)):
    print(lst[i],end=' ')