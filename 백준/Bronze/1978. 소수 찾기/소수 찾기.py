N= int(input())
lst = list(map(int,input().split()))
cnt=0
for i in range(len(lst)):
    res = []
    for j in range(1,lst[i]+1):
        if lst[i]%j==0:
            res.append(j)
    if len(res)==2:
        cnt+=1
print(cnt)