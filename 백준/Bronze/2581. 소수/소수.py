M = int(input())
N = int(input())
result = []
for i in range(M,N+1):
    lst = []
    for j in range(1,i+1):
        if i%j==0:
            lst.append(j)
    if len(lst)==2:
        result.append(i)
sum = 0
for i in range(len(result)):
    sum += result[i]
if len(result)<1:
    print(-1)
else:
    print(sum)
    print(result[0])