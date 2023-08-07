import math
def solution(fees, records):
    dic, answer = {}, []
    for record in records:
        record = record.split(" ")
        dic[record[1]] = 0

    for record in records:
        record = record.split(" ")
        if record[2] == 'IN':
            dic[record[1]] -= (int(record[0][:2])*60+int(record[0][3:]))
        elif record[2] == 'OUT':
            dic[record[1]] += (int(record[0][:2])*60+int(record[0][3:]))

    sorted_dic = dict(sorted(dic.items()))

    for i in sorted_dic:
        if sorted_dic[i]<=0:
            sorted_dic[i] += (24*60-1)
        if sorted_dic[i]<=fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil(((sorted_dic[i]-fees[0])/fees[2]))*fees[3])
            
    return answer