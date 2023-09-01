# from collections import deque
# def solution(prices):
#     prices = deque(prices)
#     answer = []
#     while prices:
#         nodrop = 0
#         price = prices.popleft()
#         if prices:
#             for i in prices:
#                 if price <= i:
#                     nodrop += 1
#                 else:
#                     price > i
#                     nodrop += 1
#                     break
#             answer.append(nodrop)
#         else:
#             answer.append(0)
            
#     return answer


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
                
    
    
    
    
    
    
    
    
    
    
    
    
    