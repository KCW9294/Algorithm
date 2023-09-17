def solution(n):
    answer = 0
    temp = ''
    while n>0:
        temp = str(n%3) + temp
        n = n//3
    length = len(temp)
    temp = temp[::-1]
    
    for i in temp:
        answer += int(i)*3**(length-1)
        length -= 1
        
    return answer