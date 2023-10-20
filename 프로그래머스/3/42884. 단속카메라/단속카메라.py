def solution(routes):
    answer = 1
    routes.sort()
    temp = routes[0][1]
    for i in range(1,len(routes)):
        if routes[i][0]>temp:
            answer += 1
            temp = routes[i][1]
        else:
            temp = min(routes[i][1],temp)
        
    return answer