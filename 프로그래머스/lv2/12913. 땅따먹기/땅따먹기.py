def solution(land):
    answer = 0

    for i in range(len(land)):
        if i==0:
            continue
        else:
            for j in range(len(land[0])):
                temp = []
                for k in range(len(land[0])):
                    if j==k:
                        continue
                    else:
                        temp.append(land[i-1][k])
                land[i][j] += max(temp)
       

    return max(land[-1])