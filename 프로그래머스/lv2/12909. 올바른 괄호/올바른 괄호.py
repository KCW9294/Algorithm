def solution(s):
    answer = True
    temp = []
    for i in range(len(s)):
        if s[0] == ')':
            answer = False
            break
        if s[i] == '(':
            temp.append(s[i])
        else:
            if len(temp)==0:
                answer = False
                break
            temp.pop()
    if len(temp) == 0 and answer == True:
        answer = True
    else:
        answer = False

    return answer