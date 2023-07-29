def solution(s):
    s = s.split(' ')
    lst = []
    for num in s:
        lst.append(int(num))
    
    answer = str(min(lst)) + " " + str(max(lst))
    return answer