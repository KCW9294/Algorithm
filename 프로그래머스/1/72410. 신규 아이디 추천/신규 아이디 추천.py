def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.':
            answer += i
        if len(answer)>=2 and i=='.':
            if answer[-2]=='.':
                answer = answer[:-1]
    if len(answer)>=1 and answer[0]=='.':
        answer = answer[1:]
    if len(answer)>=1 and answer[-1]=='.':
        answer = answer[:-1]
    if answer == '':
        answer += 'a'
    if len(answer)>=16:
        answer = answer[:15]
    if answer[-1]=='.':
        answer = answer[:-1]
    if len(answer)==1:
        answer += answer[-1]*2
    elif len(answer)==2:
        answer += answer[-1]*1
            
    return answer