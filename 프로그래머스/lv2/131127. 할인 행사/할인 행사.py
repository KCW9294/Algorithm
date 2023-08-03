def solution(want, number, discount):
    answer = 0
    for i in range(0,len(discount)-9):
        temp_count = 0
        for j in range(len(want)):
            temp = discount[i:i+10]
            if number[j] == temp.count(want[j]):
                temp_count += 1
        if temp_count == len(want):
            answer += 1
        
    
    return answer