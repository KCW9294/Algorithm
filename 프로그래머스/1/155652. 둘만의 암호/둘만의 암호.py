def solution(s, skip, index):
    s = list(s)
    for i in range(len(s)):
        temp = index
        while temp:
            if chr(ord(s[i])+1) in skip:
                s[i] = chr(ord(s[i])+1)
            else:
                s[i] = chr(ord(s[i])+1)
                if ord(s[i])>ord('z'):
                    s[i] = 'a'
                if s[i] in skip:
                    continue
                else:
                    temp -= 1
    return ''.join(s)