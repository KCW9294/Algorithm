def solution(s):
    s = s.split(" ")
    lst = []
    for word in s:
        temp = ""
        if word:
            temp = word[0].upper() + word[1:].lower()
        
        lst.append(temp)
    
    answer = " ".join(lst)

    return answer
