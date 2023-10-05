import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().rstrip().split())
star = []
weight = []
for i in range(N):
    a,b = map(int,input().rstrip().split())
    star.append([a,b])
for j in range(K):
    weight.append(int(input().rstrip()))
star.sort(key=lambda x:(x[0],-x[1]))
weight.sort()

result = []
answer = 0
for i in range(K):
    while star and weight[i]>=star[0][0]:
        heapq.heappush(result,-star[0][1])
        heapq.heappop(star)
    if  result:
        answer  -= (heapq.heappop(result))
print(answer)
    