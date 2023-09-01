from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    length = len(prices)
    while prices:
        temp = prices.popleft()
        cnt = 0
        for i in prices:
            if temp <= i:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
        
    return answer
                
    
    
    
    
    
    
    
    
    
    
    
    
    