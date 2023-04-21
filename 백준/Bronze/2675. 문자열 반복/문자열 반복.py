N = int(input())
lst = [input().split() for _ in range(N)]
for i in range(N):
    for j in range(len(lst[i][1])):
        print(int(lst[i][0])*lst[i][1][j],end='')
    print()