N = int(input())
result=[]
for i in range(N):
    x,y = map(int, input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            rst = j,k
            result.append(rst)
print(len(set(result)))