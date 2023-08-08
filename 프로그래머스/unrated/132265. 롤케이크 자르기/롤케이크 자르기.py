def solution(topping):
    answer = 0
    chul = {}
    brother = {}
    
    # 철수 딕셔너리에 토핑 추가
    for i in topping:
        if i in chul:
            chul[i] += 1
        if i not in chul:
            chul[i] = 1
    
    for i in topping:
        if i in brother:
            brother[i] += 1
        if i not in brother:
            brother[i] = 1
    
        chul[i] -= 1
        
        if chul[i] == 0:
            del chul[i]
        if len(chul) == len(brother):
            answer += 1

    return answer