def solution(a, b, n):
    answer = 0
    while True:
        temp = n%a
        n = (n//a)*b
        answer += n
        n += temp
        if n<=a-1:
            break
    return answer