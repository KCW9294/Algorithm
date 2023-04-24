N,M = map(int, input().split())
A = [input().split() for _ in range(N)]
B = [input().split() for _ in range(N)]

result = []
for i in range(N):
    lst = []
    for j in range(M):
        lst.append(int(A[i][j])+int(B[i][j]))
    result.append(lst)
    
for i in range(N):
    for j in range(M):
        print(result[i][j],end=' ')
    print()