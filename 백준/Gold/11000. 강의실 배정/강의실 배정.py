import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = []
for i in range(N):
    a,b = map(int,input().rstrip().split())
    arr.append((a,1))
    arr.append((b,-1))
arr.sort(key=lambda x:(x[0],x[1]))

result = 0
temp = 0
for _,room in arr:
    temp += room
    result = max(temp,result)
    
print(result)
