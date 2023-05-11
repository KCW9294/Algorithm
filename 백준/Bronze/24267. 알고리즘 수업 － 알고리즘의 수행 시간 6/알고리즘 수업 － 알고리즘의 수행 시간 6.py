n = int(input())
sum=0
if n==1 or n==2:
    print(0)
    print(3)
else:
    for i in range(1,n-1):
        sum += int(i*(i+1)/2)
    print(sum)
    print(3)