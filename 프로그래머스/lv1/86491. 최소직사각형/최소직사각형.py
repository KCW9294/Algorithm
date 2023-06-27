def solution(sizes):
    max_num = 1
    max_index = []
    second_max_num = 0
    for i in range(len(sizes)):
        if sizes[i][0] >= max_num:
            max_num = sizes[i][0]
            max_index = [i,0]
            second_max_num = sizes[i][1]
        if sizes[i][1] >= max_num:
            max_num = sizes[i][1]
            max_index = [i,1]
            second_max_num = sizes[i][0]
    if max_index[1] == 1:
        for j in range(len(sizes)):
            if sizes[j][0]>=second_max_num and sizes[j][1]>=second_max_num and j!=max_index[0]:
                second_max_num = min(sizes[j][0],sizes[j][1])
    else:
        for j in range(len(sizes)):
            if sizes[j][0]>=second_max_num and sizes[j][1]>=second_max_num and j!=max_index[0]:
                second_max_num = min(sizes[j][0],sizes[j][1])
    answer = max_num * second_max_num
    return answer

# 다른 사람의 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
# 미쳤다
