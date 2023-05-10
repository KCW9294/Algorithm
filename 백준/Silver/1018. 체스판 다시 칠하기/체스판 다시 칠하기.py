M,N = map(int,input().split())
lst = [input() for _ in range(M)]
result = []
for i in range(M-7):
    for j in range(N-7):
        chess1 = 0
        chess2 = 0
        
        for k in range(i,i+8):
            for q in range(j,j+8):
                if (k+q)%2==0:
                    if lst[k][q] != 'B':
                        chess1+=1
                    if lst[k][q] != 'W':
                        chess2+=1
                else:
                    if lst[k][q] != 'W':
                        chess1+=1
                    if lst[k][q] != 'B':
                        chess2+=1
        result.append(chess1)
        result.append(chess2)
print(min(result))
                        
                    