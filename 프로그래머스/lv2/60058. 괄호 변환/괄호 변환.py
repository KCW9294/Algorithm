def solution(p):
    answer = ''
    if iftrue(p)==True:
        return p
    else:
        answer = re(p)
    
    return answer
    
def split(s):
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i]=='(':
            start += 1
        else:
            end += 1
        if start == end:
            u = s[:i+1]
            v = s[i+1:] if i<len(s)-1 else "" 
            break
    return u,v

def iftrue(t):
    cnt = 0
    for i in range(len(t)):
        if t[i]=='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt<0:
            return False
    return True
        
def re(k):
    result = ""
    if len(k)==0:
        return ""
    u,v = split(k)
    if iftrue(u):
        result = u + re(v)
    else:
        temp = '('
        temp += re(v)
        temp += ')'
        for i in u[1:-1]:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        result += temp
    return result
            
        