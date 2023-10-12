def solution(ingredient):
    answer = 0
    temp = []
    for i in range(len(ingredient)):
        temp.append(ingredient[i])
        if temp[-4:] == [1,2,3,1]:
            answer += 1
            for j in range(4):
                temp.pop()
            
    return answer