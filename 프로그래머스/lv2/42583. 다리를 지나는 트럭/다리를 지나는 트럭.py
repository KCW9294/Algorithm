def solution(bridge_length, weight, truck_weights):
    temp = [0]*bridge_length
    answer = 0
    sum_weight = sum(temp)
    while len(temp):
        answer += 1
        sum_weight -= temp[0]
        temp.pop(0)
        if truck_weights:
            if sum_weight + truck_weights[0] <= weight:
                sum_weight += truck_weights[0]
                temp.append(truck_weights.pop(0))
            else:
                temp.append(0)

    return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    