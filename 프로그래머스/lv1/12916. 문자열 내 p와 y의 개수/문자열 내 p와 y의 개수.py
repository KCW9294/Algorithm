def solution(s):
    answer = 0
    for i in s:
        if i.lower() == 'p':
            answer+=1
        elif i.lower() == 'y':
            answer-=1
    if answer == 0:
        return True
    else:
        return False
    
