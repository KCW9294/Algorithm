def solution(n):
    answer = 0
    temp1 = 1
    temp2 = 2
    for i in range(3,n+1):
        answer = temp1 + temp2
        temp1 = temp2
        temp2 = answer
    return answer%1000000007