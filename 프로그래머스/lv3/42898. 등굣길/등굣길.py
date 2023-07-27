def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] 
    lst = [[0] * (m+1) for _ in range(n+1)]
    lst[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            if [i,j] in puddles:
                continue
            lst[i][j] = lst[i-1][j] + lst[i][j-1]

    answer = lst[n][m]%1000000007
    return answer