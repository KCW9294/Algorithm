N = int(input())
lst = [list(map(int, input().split())) for i in range(N)]
lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])

cnt = 1
end = lst[0][1]

for i in range(1,N):
    if lst[i][0]>=end:
        cnt+=1
        end = lst[i][1]
        
print(cnt)