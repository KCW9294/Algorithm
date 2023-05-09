N, M = map(int,input().split())
lst = list(map(int, input().split()))
max=0
sum=0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        for k in range(j+1,len(lst)):
            sum=lst[i]+lst[j]+lst[k]
            if sum<=M and sum>=max:
                max=sum
print(max)