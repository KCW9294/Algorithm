N = int(input())
lst = [int(input()) for i in range(N)]
for i in range(len(lst)):
    print(lst[i]//25, end=' ')
    lst[i]%=25
    print(lst[i]//10, end=' ')
    lst[i]%=10
    print(lst[i]//5, end=' ')
    lst[i]%=5
    print(lst[i]//1)
    lst[i]%=1