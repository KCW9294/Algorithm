def solution(ingredient):
    answer = 0
    temp = []
    for i in range(len(ingredient)):
        temp.append(ingredient[i])
        if temp[-1]==1 and len(temp)>=4:
            if temp[-4]==1 and temp[-3]==2 and temp[-2]==3:
                temp.pop()
                temp.pop()
                temp.pop()
                temp.pop()
                answer += 1
            
    return answer