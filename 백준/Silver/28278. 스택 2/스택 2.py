import sys

input = sys.stdin.readline

N = int(input())
do = [list(map(int, input().split())) for _ in range(N)]

stack = []
for i in do:
    if i[0]==1:
        stack.append(i[1])
    elif i[0]==2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif i[0]==3:
        print(len(stack))
    elif i[0]==4:
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)