n = int(input())
lst = [input() for _ in range(n)]
for i in range(n):
    print(f'{lst[i][0]}{lst[i][-1]}')