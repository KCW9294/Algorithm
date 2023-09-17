def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in d:
        if budget<0:
            return answer-1
        budget -= i
        answer += 1
        
    if budget<0:
        return answer-1
    else:  
        return answer