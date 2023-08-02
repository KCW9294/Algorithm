def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        if i//n<=i%n:
            answer.append(i%n+1)
        else:
            answer.append(i//n+1)
        
    return answer