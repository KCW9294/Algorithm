def solution(n, m, section):
    answer = 0
    temp = 0
    # 오름차순이므로 값을 순서대로 꺼내줌
    for i in section:
        # temp보다 작거나 같으면 이미 칠해진 구역이라 판단하고 continue
        if i<=temp:
            continue
        # i값이 temp보다 크면 temp를 다시 초기화해주고 페인트칠 횟수를 증가시켜줌
        else:
            # temp를 section에서 꺼낸 구역 번호 + 롤러 길이 값이라 지정
            temp = i+m-1
            answer += 1
    return answer