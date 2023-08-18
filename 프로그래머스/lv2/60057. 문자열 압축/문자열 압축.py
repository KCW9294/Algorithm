def solution(s):
    answer = []
    for i in range(1,len(s)+1):
        alz = ''
        cnt = 1
        temp = s[:i]
        
        for j in range(i,len(s)+i,i):
            if s[j:j+i]==temp:
                cnt += 1
            else:
                if cnt!=1:
                    alz = alz+str(cnt)+temp
                else:
                    alz = alz + temp
                cnt = 1
                temp = s[j:j+i]
        
        answer.append(len(alz))
        
    return min(answer)