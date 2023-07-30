def solution(n):
    num1 = 0
    num2 = 1
    for i in range(2, n+1):
        answer = num1 + num2
        num1 = num2
        num2 = answer

    return answer%1234567