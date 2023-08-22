def solution(n):
    answer = []
    lst = [[0]*n for _ in range(n)]
    x= -1
    y= 0
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                x+=1
            if i%3==1:
                y+=1
            if i%3==2:
                x-=1
                y-=1
            lst[x][y] = num
            num += 1
    
    for i in lst:
        for j in i:
            if j:
                answer.append(j)
    
    return answer