def solution(n, t, m, p):
    answer = ''
    temp = '0'
    for i in range(t*m):
        rev_base = ''
        while i > 0:
            i, mod = divmod(i, n)
            if mod>=10:
                if mod==10:
                    rev_base += 'A'
                if mod==11:
                    rev_base += 'B'
                if mod==12:
                    rev_base += 'C'
                if mod==13:
                    rev_base += 'D'
                if mod==14:
                    rev_base += 'E'
                if mod==15:
                    rev_base += 'F'
            else:
                rev_base += str(mod)
        temp += rev_base[::-1] 
    
    for j in range(len(temp)):
        if j%m==p-1:
            answer += temp[j]
        if len(answer) == t:
            break
    
    return answer