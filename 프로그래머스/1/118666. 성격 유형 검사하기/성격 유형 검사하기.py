def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    
    for i in range(len(survey)):
        if choices[i]<=3:
            dic[survey[i][0]] += score[choices[i]]
        elif choices[i]>=5:  
            dic[survey[i][1]] += score[choices[i]]
            
    if dic['R']>=dic['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if dic['C']>=dic['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dic['J']>=dic['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if dic['A']>=dic['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer