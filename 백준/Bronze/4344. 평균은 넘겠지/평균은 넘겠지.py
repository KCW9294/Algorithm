N = int(input())
lst = [input().split() for _ in range(N)]
sum = 0
sol = []
for i in range(N):
    sum=0
    for j in range(1,len(lst[i])):
        sum+=int(lst[i][j])
    sol.append(sum/int(lst[i][0]))
result = []
for i in range(N):
    count=0
    for j in range(1, len(lst[i])):
        if int(lst[i][j])>sol[i]:
            count+=1
    result.append(round(count/int(lst[i][0])*100,3))
for i in range(N):
    print(f"{result[i]:.3f}%")