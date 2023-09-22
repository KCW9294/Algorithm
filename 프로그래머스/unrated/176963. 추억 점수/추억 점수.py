def solution(name, yearning, photo):
    answer = [0]*len(photo)
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in range(len(photo)):
        for j in photo[i]:
            if j not in dic:
                continue
            else:
                answer[i] += dic[j]
    return answer