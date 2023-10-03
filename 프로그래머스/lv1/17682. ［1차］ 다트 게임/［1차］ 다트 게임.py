def solution(dartResult):
    answer = 0
    temp = []
    temp_temp = ''
    for i in range(len(dartResult)):
        if i==0:
            temp_temp = dartResult[i]
        else:
            if dartResult[i].isdigit():
                if len(temp_temp)==1:
                    temp_temp += dartResult[i]
                else:
                    temp.append(temp_temp)
                    temp_temp = ''
                    temp_temp += dartResult[i]
            elif dartResult[i].isalpha():
                if dartResult[i]=='D':
                    temp_temp += '**2'
                elif dartResult[i]=='T':
                    temp_temp += '**3'
                else:
                    temp_temp += '**1'
            else:
                if dartResult[i]=='*':
                    if temp:
                        temp[-1] = temp[-1]+'*2'
                        temp_temp += '*2'
                    else:
                        temp_temp += '*2'
                else:
                    temp_temp += '*(-1)'
            if i==len(dartResult)-1:
                temp.append(temp_temp)
    for i in temp:
        answer += eval(i)
    return answer