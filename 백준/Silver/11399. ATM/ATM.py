N = int(input())
lst = list(map(int,input().split()))

lst.sort()
cnt = 0
for i in range(len(lst)):
    cnt += lst[i]*(len(lst)-i)
print(cnt)