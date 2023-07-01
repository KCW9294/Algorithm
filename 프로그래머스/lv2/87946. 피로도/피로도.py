from itertools import permutations

def solution(k, dungeons):
    dungeons_len = len(dungeons)
    answer = 0
    for per in permutations(dungeons, dungeons_len):
        hp = k
        cnt = 0
        for p in per:
            if hp >= p[0]:
                hp -= p[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer