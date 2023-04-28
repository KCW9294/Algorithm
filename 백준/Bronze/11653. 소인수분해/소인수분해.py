N = int(input())
for i in range(2,N+1):
    if N%i == 0:
        N=N/i
        print(i)
        while(N%i==0):
            if N%i == 0:
                N=N/i
                print(i)
            else:
                break