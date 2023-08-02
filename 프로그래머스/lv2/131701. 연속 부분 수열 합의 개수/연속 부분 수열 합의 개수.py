def solution(elements):
    answer = []
    tuning_elements = elements + elements
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            answer.append(sum(tuning_elements[j:j+i]))
            
    answer = len(set(answer))
    return answer