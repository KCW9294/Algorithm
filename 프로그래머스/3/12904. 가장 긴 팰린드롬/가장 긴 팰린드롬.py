def solution(s):
    answer = [1]
    for i in range(1,len(s)):
        temp = 2
        while True:
            if i-temp==-1:
                if s[i::-1] == s[i:i+temp]:
                    answer.append((temp-1)*2+1)
                    break
                else:
                    break
            else:
                if s[i:i-temp:-1] == s[i:i+temp]:
                    answer.append((temp-1)*2+1)
                else:
                    break
            temp += 1
            
    for i in range(0,len(s)-1):
        temp = 1
        while True:
            if i-temp==-1:
                if s[i::-1] == s[i+1:i+temp+1]:
                    answer.append((temp)*2)
                    break
                else:
                    break
            else:
                if s[i:i-temp:-1] == s[i+1:i+temp+1]:
                    answer.append((temp)*2)
                else:
                    break
            temp += 1
            
    return max(answer)