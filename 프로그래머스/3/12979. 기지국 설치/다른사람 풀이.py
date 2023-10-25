import math
def solution(n, stations, w):
    answer, start = 0, 1
    for c in stations:
        answer += math.ceil(((c - w) - start)/(2 * w + 1))
        start = c + w + 1
    answer += math.ceil((n + 1 - start)/(2 * w + 1))
    return answer
