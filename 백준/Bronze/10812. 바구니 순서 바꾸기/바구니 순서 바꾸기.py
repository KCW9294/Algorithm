N,M=map(int,input().split())
lst=[]
for i in range(1,N+1):
    lst.append(i)
for i in range(M):
    begin,end,mid = map(int, input().split())
    lst = lst[:begin-1] + lst[mid-1:end] + lst[begin-1:mid-1] + lst[end:]
for i in range(len(lst)):
    print(lst[i],end=' ')