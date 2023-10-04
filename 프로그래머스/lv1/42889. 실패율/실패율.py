def solution(N, stages):
    answer = []
    people = len(stages)
    result = []
    for i in range(1,N+1):
        if people == 0:
            answer.append((i,0))
            continue
        temp = stages.count(i)
        answer.append((i,temp/people))
        people -= temp
    answer.sort(key=lambda x:(-x[1],x[0]))
    for i,j in answer:
        result.append(i)
    return result