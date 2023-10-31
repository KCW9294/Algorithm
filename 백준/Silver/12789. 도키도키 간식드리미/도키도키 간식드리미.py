from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst = deque(lst)

stack = []
order = 1

while True:
    if lst and lst[0]==order:
        lst.popleft()
        order += 1
    else:
        if stack and stack[-1]==order:
            stack.pop()
            order += 1
        else:
            if not lst:
                break
            stack.append(lst.popleft())
if not lst and not stack:
    print("Nice")
else:
    print("Sad")
