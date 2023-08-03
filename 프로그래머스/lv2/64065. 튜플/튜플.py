def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    temp = []
    for i in s:
        i = i.replace(","," ")
        i = i.split(" ")
        temp_temp = []
        for j in i:
            temp_temp.append(int(j))
        temp.append(temp_temp)
    temp.sort(key=lambda x:len(x))
    for k in temp:
        for m in k:
            if m not in answer:
                answer.append(m)
        
    return answer