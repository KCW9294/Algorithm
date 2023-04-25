while(True):
    N = int(input())
    if N==-1:
        break
    lst=[]
    for i in range(1,N):
        if N%i==0:
            lst.append(i)
    sum=0
    for i in lst:
        sum+=i
    if sum==N:
        print(f"{N} =",end=' ')
        for i in range(len(lst)):
            if (i+1)==len(lst):
                print(f'{lst[i]}')
            else:
                print(f'{lst[i]} +',end=' ')
    else:
        print(f'{N} is NOT perfect.')