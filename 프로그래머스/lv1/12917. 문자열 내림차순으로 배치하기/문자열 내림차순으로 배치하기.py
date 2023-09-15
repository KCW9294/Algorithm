def solution(s):
    s = list(map(str,s))
    s.sort(reverse=True)
    return ''.join(s)