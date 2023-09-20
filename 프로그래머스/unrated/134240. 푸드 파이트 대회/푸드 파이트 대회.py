def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += f'{i}'*(food[i]//2)
    answer += "0"
    for i in range(len(food)-1,-1,-1):
        answer += f'{i}'*(food[i]//2)
    return answer