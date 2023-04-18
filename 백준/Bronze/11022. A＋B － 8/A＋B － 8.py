import sys
N = int(input())
sum=[]
temp1=[]
temp2=[]
for i in range(1,N+1):
    A,B=map(int, sys.stdin.readline().split())
    sum.append(A+B)
    temp1.append(A)
    temp2.append(B)
for i in range(N):
    print(f'Case #{i+1}: {temp1[i]} + {temp2[i]} = {sum[i]}')
