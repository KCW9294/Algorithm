import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    a,b = map(int,input().rstrip().split())
    arr.append((a,1)) # 선분 시작
    arr.append((b,-1)) # 선분 끝
    
arr.sort()
result = 0
temp = 0
for x,point in arr:
    temp += point
    result = max(result,temp)

print(result)
    
    