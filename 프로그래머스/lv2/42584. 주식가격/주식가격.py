from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        nodrop = 0
        price = prices.popleft()
        if prices:
            for i in prices:
                if price <= i:
                    nodrop += 1
                else:
                    price > i
                    nodrop += 1
                    break
            answer.append(nodrop)
        else:
            answer.append(0)
            
    return answer