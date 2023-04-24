N = [list(map(int,input().split())) for _ in range(9)]
max = 0
for i in range(9):
    for j in range(9):
        if N[i][j]>max:
            max = N[i][j]
for i in range(9):
    for j in range(9):
        if N[i][j] == max:
            a,b=i,j
print(max)
print(a+1,b+1)