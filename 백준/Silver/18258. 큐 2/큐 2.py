import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
que = deque()
for _ in range(N):
    order = input().split()
    if order[0]=='push':
        que.append(order[1])
    elif order[0]=='front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif order[0]=='back':
        if que:
            print(que[-1])
        else:
            print(-1)
    elif order[0]=='size':
        print(len(que))
    elif order[0]=='pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    else:
        if que:
            print(0)
        else:
            print(1)