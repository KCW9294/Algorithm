def solution(data, col, row_begin, row_end):
    answer = 0
    temp = []
    data.sort(key=lambda x:x[0], reverse=True)
    data.sort(key=lambda x:x[col-1])
    for i in range(row_begin, row_end+1):
        temp_temp = 0
        for k in data[i-1]:
            temp_temp += k%i
        temp.append(temp_temp)
    for i in temp:
        answer = answer^i
    return answer