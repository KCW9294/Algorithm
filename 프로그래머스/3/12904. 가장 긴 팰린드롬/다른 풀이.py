def solution(s):
    if len(s) <= 1:
        return len(s)
    
    max_length = 1  # 최소한 1글자는 팰린드롬

    for i in range(1, len(s)):
        # 홀수 길이의 팰린드롬 확인
        left, right = i - 1, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            max_length = max(max_length, right - left + 1)
            left -= 1
            right += 1

        # 짝수 길이의 팰린드롬 확인
        left, right = i - 1, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            max_length = max(max_length, right - left + 1)
            left -= 1
            right += 1

    return max_length
