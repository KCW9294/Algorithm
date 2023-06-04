for T in range(int(input())):
    N,M = map(int, input().split())
    arr = list(map(int,input().split()))
    lst = []
    array1 = []
    max_num = 0
    for i in range(N):
        for j in range(M):
            lst.append(arr[j+i*4])
        array1.append(lst)
        lst = []
    for i in range(N):
        for j in range(1,M):
            if i-1<0:
                array1[i][j] = array1[i][j] + max(array1[i][j-1],array1[i+1][j-1])
            elif i+1>=N:
                array1[i][j] = array1[i][j] + max(array1[i-1][j-1],array1[i][j-1])
            else:
                array1[i][j] = array1[i][j] + max(array1[i-1][j-1],array1[i][j-1],array1[i+1][j-1])
            if array1[i][j]>=max_num:
                max_num = array1[i][j]
    print(max_num)