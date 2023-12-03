N, M = map(int, input().split())
lst = []
answer = 0
for i in range(N):
    lst.append(input())
for i in range(M):
    word = input()
    if word in lst:
        answer += 1
print(answer)