def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    temp = len(score)//m
    for i in range(1,temp+1):
        answer += score[m*i-1]*m
        
    return answer