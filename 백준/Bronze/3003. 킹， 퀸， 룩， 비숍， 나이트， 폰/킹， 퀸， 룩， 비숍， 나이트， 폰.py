n = list(map(int,input().split()))
m = [1,1,2,2,2,8]
result = [0 for _ in range(6)]
for i in range(len(n)):
    if n[i]-m[i]==0:
        continue
    else:
        result[i]=m[i]-n[i]
for i in range(len(n)):
    print(result[i],end=' ')