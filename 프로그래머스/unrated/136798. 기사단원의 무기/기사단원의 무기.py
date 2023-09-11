def solution(number, limit, power):
    lst = []
    for i in range(1,number+1):
        temp = 0
        if i**0.5==round(i**0.5,0):
            for k in range(1,int(i**0.5)):
                if i%k==0:
                    temp += 1
            lst.append(temp*2+1)
        else:
            for j in range(1,int(i**0.5+1)):
                if i%j==0:
                    temp += 1
            lst.append(temp*2)
    lst.sort()
    for i in range(len(lst)):
        if lst[i]>limit:
            return sum(lst[:i])+(len(lst)-i)*power
    return sum(lst)