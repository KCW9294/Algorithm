def solution(data, col, row_begin, row_end):
    answer = 0
    temp = []
    # col번째 컬럼의 값 기준으로 오름차순 정렬후 첫 번째 컬럼 값 기준으로 내림차순 정렬
    data.sort(key=lambda x:[x[col-1],-x[0]])
    for i in range(row_begin, row_end+1):
        temp_temp = 0
        for k in data[i-1]:
            temp_temp += k%i
        temp.append(temp_temp)
    for i in temp:
        answer = answer^i
    return answer