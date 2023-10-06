N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
dp = [0]*N

if len(lst)<=2:
    print(sum(lst))
else:
    dp[0] = lst[0]
    dp[1] = lst[0]+lst[1]
    dp[2] = max(lst[0]+lst[2],lst[1]+lst[2])
    for i in range(3,len(lst)):
        dp[i] = max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i])
    print(dp[-1])