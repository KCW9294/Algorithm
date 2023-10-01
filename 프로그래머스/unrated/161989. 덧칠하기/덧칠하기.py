def solution(n, m, section):
    answer = 0
    temp = 0
    for i in section:
        if i<=temp:
            continue
        else:
            temp = i+m-1
            answer += 1
    return answer