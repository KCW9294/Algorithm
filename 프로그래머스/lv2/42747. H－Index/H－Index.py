def solution(citations):
    answer=[]
    for i in range(10001):
        cnt=0
        cnt2=0
        for j in citations:
            if i >= j:
                cnt+=1
            if i <= j:
                cnt2+=1
        if i>=cnt and i<=cnt2:
            answer.append(i)
        if i == 0:
            answer.append(i)
    answer.sort(reverse=True)
    answer = answer[0]
    return answer
