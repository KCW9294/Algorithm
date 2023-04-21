N,M = map(int, input().split())
lst = [_ for _ in range(1,N+1)]

for i in range(M):
    x,y=map(int, input().split())
    if x==1:
        lst[x-1:y] = lst[y-1::-1]
    else:
        lst[x-1:y] = lst[y-1:x-2:-1]
for i in range(N):
    print(lst[i],end=' ')