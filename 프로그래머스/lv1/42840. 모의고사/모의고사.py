def solution(answers):
    lst_1 = [1,2,3,4,5]*2000
    lst_2 = [2,1,2,3,2,4,2,5]*1250
    lst_3 = [3,3,1,1,2,2,4,4,5,5]*1000
    result = [[1,0],[2,0],[3,0]]
    answer = []
    for i in range(len(answers)):
        if answers[i] == lst_1[i]:
            result[0][1] += 1
        if answers[i] == lst_2[i]:
            result[1][1] += 1
        if answers[i] == lst_3[i]:
            result[2][1] += 1
    result.sort(key=lambda x: (-x[1], x[0]))
    if result[0][1]==result[1][1] and result[0][1]!=result[2][1]:
        answer.append(result[0][0])
        answer.append(result[1][0])
    elif result[0][1]==result[2][1]:
        for i in range(len(result)):
            answer.append(result[i][0])
    else:
        answer.append(result[0][0])
    return answer