N = int(input())
n_sum=0
for i in range(1,N+1):
    n_sum = sum(map(int,str(i)))
    result = i+n_sum
    if result == N:
        print(i)
        break
    elif i == N:
        print(0)