N = int(input())
M = set()
for i in range(N):
    M.add(int(input()))
M = list(M)
M.sort()
for i in range(len(M)):
    print(M[i])