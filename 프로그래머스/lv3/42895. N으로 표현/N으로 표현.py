def solution(N, number):
    dp = []
    
    for i in range(1,9):
        temp = []
        temp.append(int(str(N)*i))
        
        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    temp.append(op1+op2)
                    temp.append(op1-op2)
                    temp.append(op1*op2)
                    if op2 != 0:
                        temp.append(int(op1/op2))
                    
        if number in temp:
            return i
            break
        
        else:
            dp.append(temp)
            
    return -1