def solution(n):
    temp = []
    for i in str(n):
        temp.append(i)
    temp.sort(reverse=True)
    return int(''.join(temp))