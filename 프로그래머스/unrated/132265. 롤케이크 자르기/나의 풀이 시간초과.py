from collections import deque
def solution(topping):
    answer = 0
    topping = deque(topping)
    chul, brother = set(), set()
    length = len(topping)
    for i in range(length):
        chul.add(topping.popleft())
        brother = set(topping)
        if len(chul) == len(brother):
            answer += 1
    
    return answer
