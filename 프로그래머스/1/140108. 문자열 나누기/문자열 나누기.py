def solution(s):
    answer = 0
    while s:
        cnt = 0
        if len(s)==1:
            answer += 1
            break
        else:
            for i in range(len(s)):
                temp = s[0]
                if temp==s[i]:
                    cnt += 1
                elif temp!=s[i]:
                    cnt -= 1
                if cnt==0:
                    if i!=len(s)-1:
                        s = s[i+1:]
                        answer += 1
                        break
                    else:
                        s = ''
                        answer += 1
                        break
                if i==len(s)-1:
                    s = ''
                    answer += 1
                    break

    return answer