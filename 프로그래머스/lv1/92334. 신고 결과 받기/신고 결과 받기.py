def solution(id_list, report, k):
    dic = {}
    cnt = {}
    answer = {}
    temp = []
    for i in id_list:
        cnt[i] = 0
        answer[i] = 0

    for i in set(report):
        x,y = i.split(" ")
        if x not in dic:
            dic[x] = [y]
            cnt[y] += 1
        else:
            dic[x].append(y)
            cnt[y] += 1

    for i in cnt:
        if cnt[i]>=k:
            temp.append(i)
    
    for i in dic:
        for j in temp:
            if j in dic[i]:
                answer[i] += 1
    
    result = []
    for i in id_list:
        result.append(answer[i])
    return result