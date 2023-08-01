def solution(k, tangerine):
    answer = []
    temp = set(tangerine)
    cnt = [0]*(max(tangerine)+1)
    lst = []
    for i in tangerine:
        cnt[i] += 1
    
    for i in tangerine:
        lst.append((cnt[i],i))
        
    lst.sort(key=lambda x: x[1])
    lst.sort(key=lambda x: -x[0])
    
    for i in lst:
        answer.append(i[1])
        if len(answer) == k:
            break
    
    return len(set(answer))