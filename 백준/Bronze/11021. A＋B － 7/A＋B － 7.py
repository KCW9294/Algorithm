import sys
N = int(input())
sum=[]
for i in range(1,N+1):
    A,B=map(int, sys.stdin.readline().split())
    sum.append(A+B)
for i in range(N):
    print(f'Case #{i+1}: {sum[i]}')