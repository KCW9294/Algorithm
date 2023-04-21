N = int(input())
lst = list(map(int,input().split()))
max = lst[0]
sum=0
new = []
for i in range(len(lst)):
    if lst[i]>max:
        max=lst[i]
for i in range(len(lst)):
    new.append(lst[i]/max*100)
for i in range(len(lst)):
    sum += new[i]
print(sum/N)