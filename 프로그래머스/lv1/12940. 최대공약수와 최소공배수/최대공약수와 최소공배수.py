def solution(n, m):
    answer = []
    temp1 = []
    temp2 = []
    for i in range(1,n+1):
        if n%i==0:
            temp1.append(i)
    for i in range(1,m+1):
        if m%i==0:
            temp2.append(i)
            
    if n>m:
        for i in temp2[::-1]:
            if i in temp1:
                answer.append(i)
                break
    else:
        for j in temp1[::-1]:
            if j in temp2:
                answer.append(j)
                break
    
    answer.append(n*m//answer[-1])
    
    return answer