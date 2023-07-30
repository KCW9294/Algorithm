def solution(n):
    answer = 0
    k = 1
    break_second = False
    while k != n+1:
        num = []
        cnt = 0
        for i in range(k,n+1):
            num.append(i)
            cnt += 1
            if len(num) == cnt and sum(num) == n:
                answer += 1
                break
            if sum(num) > n:
                break
        k += 1
        
    return answer