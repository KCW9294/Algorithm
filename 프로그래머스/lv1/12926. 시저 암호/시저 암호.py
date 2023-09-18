def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                if chr(ord(i)+n).isalpha() and chr(ord(i)+n).isupper():
                    answer += chr(ord(i)+n)
                else:
                    answer += chr(ord('A')+n-(ord('Z')-ord(i))-1)
            else:
                if chr(ord(i)+n).isalpha():
                    answer += chr(ord(i)+n)
                else:
                    answer += chr(ord('a')+n-(ord('z')-ord(i))-1)
        else:
            answer += i              
    return answer