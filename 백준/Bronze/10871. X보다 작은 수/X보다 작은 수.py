N,M = map(int,input().split())
lst = input().split()
result=[]
for i in range(len(lst)):
    if M>int(lst[i]):
        print(lst[i],end=' ')