N, K = map(int, input().split())
lst = [int(input()) for i in range(N)]
result = 0
for i in reversed(range(N)):
    result += K//lst[i]
    K = K%lst[i]
    if K == 0:
        break
print(result)    