def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    else:
        if s%n==0:
            for i in range(n):
                answer.append(s//n)
        else:
            for i in range(n-s%n):
                answer.append(s//n)
            for i in range(s%n):
                answer.append(s//n+1)
    return answer