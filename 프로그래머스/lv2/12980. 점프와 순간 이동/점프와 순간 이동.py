def solution(n):
    answer = 0
    while n:
        if n%2 == 0:
            n = n//2
        else:
            answer+=1
            n = (n-1)//2

    return answer