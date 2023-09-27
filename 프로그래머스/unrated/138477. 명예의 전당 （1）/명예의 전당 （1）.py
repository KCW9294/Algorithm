import heapq
def solution(k, score):
    answer = []
    temp = []
    for i in score:
        if len(temp) == k:
            if i < temp[0]:
                answer.append(temp[0])
            else:
                heapq.heappop(temp)
                heapq.heappush(temp, i)
                answer.append(temp[0])
        else:
            heapq.heappush(temp,i)
            answer.append(temp[0])

    return answer