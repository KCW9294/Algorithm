def solution(n):
    answer = 0
    if n**0.5 == round(n**0.5,0):
        return (n**0.5+1)**2
    else:
        return -1