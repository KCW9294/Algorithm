def solution(genres, plays):
    answer = []
    genres_dic = {}
    plays_dic = {}
    for i in list(set(genres)):
        plays_dic[i] = []
    
    for i in range(len(genres)):
        if genres[i] not in genres_dic:
            genres_dic[genres[i]] = plays[i]
            plays_dic[genres[i]].append((plays[i],i))
        else:
            genres_dic[genres[i]] += plays[i]
            plays_dic[genres[i]].append((plays[i],i))

    temp = sorted(genres_dic.items(), key=lambda x:-x[1])
    temp2 = sorted(plays_dic.items())
    for i in temp:
        for j in temp2:
            if i[0]==j[0]:
                temp3 = j[1]
                temp3.sort(key=lambda x:-x[0])
                if len(j[1])==1:
                    answer.append(temp3[0][1])
                else:
                    answer.append(temp3[0][1])
                    answer.append(temp3[1][1])
    return answer