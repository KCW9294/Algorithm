def solution(priorities, location):
    deq = [(i,j) for i,j in enumerate(priorities)]
    answer = 0
    while deq:
        go = True
        temp = deq.pop(0)
        for i in deq:
            if temp[1] < i[1]:
                deq.append(temp)
                go = False
                break
        if go == True:
            answer += 1
            if temp[0] == location:
                return answer

    return answer