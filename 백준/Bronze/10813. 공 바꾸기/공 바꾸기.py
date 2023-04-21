N,M = map(int,input().split())
lst = [_ for _ in range(1,N+1)]
for i in range(M):
    x, y = map(int, input().split())
    temp = lst[x-1]
    lst[x-1] = lst[y-1]
    lst[y-1] = temp
for i in range(N):
    print(lst[i],end=' ')