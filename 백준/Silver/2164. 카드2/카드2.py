from collections import deque

N = int(input())
stack = [i for i in range(1,N+1)]
stack = deque(stack)

while True:
    if len(stack)==1:
        print(stack[0])
        break
    else:
        stack.popleft()
        stack.append(stack.popleft())
    
