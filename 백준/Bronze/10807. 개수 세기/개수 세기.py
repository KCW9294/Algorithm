N = int(input())
lst=input().split()
K = str(input())
count=0
for i in range(len(lst)):
    if K == lst[i]:
        count+=1
print(count)