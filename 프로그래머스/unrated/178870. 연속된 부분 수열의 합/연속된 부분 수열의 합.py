def solution(sequence, k):
    answer = []
    
    start = 0
    end = 0
    sum_ = 0
    
    while True:
        if sum_<=k:
            if sum_==k:
                answer.append((start,end-1))
            if end == len(sequence):
                break
            sum_+=sequence[end]
            end += 1
        else:
            sum_-=sequence[start]

            if start == len(sequence):
                break
            start += 1
    
    answer = sorted(answer,key=lambda x:(x[1]-x[0],x[0]))
    
    return answer[0]