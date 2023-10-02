def solution(k, d):
    answer = 0
    coordinate = []
    # d//k를 구하여 x,y 각각이 d길이보다 작은 모든 좌표를 구해준다
    for i in range(d//k+1):
        for j in range(d//k+1):
            coordinate.append((i*k,j*k))
    # 거리계산을 하여 d값보다 작은 경우 answer += 1을 해준다.
    for x,y in coordinate:
        if (x*x+y*y)**0.5<=d:
            answer += 1
          
    return answer
