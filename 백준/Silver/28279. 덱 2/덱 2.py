from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
commands = [list(map(int,input().split())) for _ in range(N)]

deck = deque()  # 덱 생성

result = []
for command in commands:
    if command[0] == 1:
        x = command[1]
        deck.appendleft(x)  # 1 X: 정수 X를 덱의 앞에 넣는다.
    elif command[0] == 2:
        x = command[1]
        deck.append(x)  # 2 X: 정수 X를 덱의 뒤에 넣는다.
    elif command[0] == 3:
        if deck:
            print(deck.popleft())  # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다.
        else:
            print(-1)
    elif command[0] == 4:
        if deck:
            print(deck.pop())  # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다.
        else:
            print(-1)
    elif command[0] == 5:
        print(len(deck))  # 5: 덱에 들어있는 정수의 개수를 출력한다.
    elif command[0] == 6:
        if not deck:
            print(1)
        else:
            print(0) # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
    elif command[0] == 7:
        if deck:
            print(deck[0])  # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다.
        else:
            print(-1)
    elif command[0] == 8:
        if deck:
            print(deck[-1])  # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다.
        else:
            print(-1)