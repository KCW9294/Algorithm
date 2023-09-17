def solution(s):
    answer = []
    s = s.split(" ")
    for word in s:
        temp = ""
        for i in range(len(word)):
            if (i)%2==0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
    return ' '.join(answer)