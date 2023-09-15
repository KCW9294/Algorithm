def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            if i.isalpha():
                return False
        return True
    else:
        return False