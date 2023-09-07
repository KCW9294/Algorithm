import heapq
def solution(N, road, K):
    answer = []
    node = [[] for _ in range(N+1)]
    distance = [1000000000]*(N+1)
    
    for a,b,c in road:
        node[a].append((b,c))
        node[b].append((a,c))
    
        
    q = []
    heapq.heappush(q, (0,1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in node[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    for i in range(1, N+1):
        if distance[i] <= K:
            answer.append(i)
    print(answer)

    q = []
    heapq.heappush(q,5)
    print(q)
    heapq.heappush(q,1)
    print(q)
    return len(answer)