def solution(n):
    answer = 0
    for i in range(2,n+1):
        cnt = 0
        for j in range(2,int(i**0.5+1)):
            if i%j==0:
                cnt += 1
            if cnt>0:
                break
        if cnt == 0:
            answer += 1
    return answer