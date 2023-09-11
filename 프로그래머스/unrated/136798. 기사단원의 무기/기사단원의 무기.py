def solution(number, limit, power):
    lst = []
    for i in range(1,number+1):
        temp = 0
        for j in range(1,int(i**0.5+1)):
            if i**0.5==j:
                temp += 1
            elif i%j==0:
                temp += 2
        lst.append(temp)
    lst.sort()
    for i in range(len(lst)):
        if lst[i]>limit:
            return sum(lst[:i])+(len(lst)-i)*power
    return sum(lst)