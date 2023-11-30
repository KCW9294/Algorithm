N = int(input())
lst = []
for i in range(N):
    lst.append((input().split()))
lst.sort(key=lambda x:int(x[0]))

for x,y in lst:
    print(x+' '+y)
