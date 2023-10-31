import sys

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
stack = []

for i in lst:
    if i==0:
        if stack:
            stack.pop()
    else:
        stack.append(i)
        
print(sum(stack))