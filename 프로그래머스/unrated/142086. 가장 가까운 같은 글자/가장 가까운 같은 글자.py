def solution(s):
    answer = []
    for i in range(len(s)):
        cnt = 0
        for j in range(i-1,-1,-1):
            if s[j]==s[i]:
                cnt = i-j
                break
        if cnt != 0:
            answer.append(cnt)
        else:
            answer.append(-1)
        
    return answer