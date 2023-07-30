def solution(s):
    if len(s)%2 == 1: 
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    
    stack = [s[0]]
    
    for i in range(1,len(s)):
        if len(stack) > 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if len(stack)!=0:
        return 0
    else:
        return 1
