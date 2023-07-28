def solution(n, times):
    left = min(times)  # 범위의 왼쪽 값
    right = max(times)*n  # 범위의 오른쪽 값
    mid = 0  
    answer = 0
     
    while left <= right: # left값과 right값이 달라질때까지 반복
        mid = (left + right) // 2  # 중간값
        temp = 0
        
        for time in times:
            temp += mid//time
            if temp >= n:  # 총 응대한 인원수가 n보다 크거나 같으면 빨리 탈출
                break
        
        if temp >= n:   # 응대한 인원이 n보다 크거나 같으면
            right = mid-1  # right 범위를 mid-1로 줄여줌
            answer = mid
        else:  # temp < n
            left = mid+1
    
    return answer