def solution(weights):
    answer = 0
    
    dic = {}
    
    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

            
    for i in dic:
        if dic[i] > 1:
            answer += (dic[i] * (dic[i]-1)) / 2
        if i*2 in dic:
            answer += dic[i] * dic[2*i]
        if i*3/2 in dic:
            answer += dic[i] * dic[i*3/2]
        if i*4/3 in dic:
            answer += dic[i] * dic[i*4/3]
            
    return answer