import sys, heapq
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

INF = int(10**9)
distance = [INF]*(V+1)

def dijstra(start):
    Q = []
    distance[start] = 0
    heapq.heappush(Q, (0,start))
    while Q:
        now_cost, now_node = heapq.heappop(Q)
        for next_cost, next_node in graph[now_node]:
            if next_cost + now_cost < distance[next_node]:
                next_cost = next_cost + now_cost
                distance[next_node] = next_cost
                heapq.heappush(Q, (next_cost, next_node))

dijstra(K)

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])