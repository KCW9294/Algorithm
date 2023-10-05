import sys  
input = sys.stdin.readline  

T = int(input().rstrip())  
for _ in range(T):  
    result = 1
    N = int(input().rstrip())  
    arr = []  
    for _ in range(N):  
        a,b = map(int,input().rstrip().split())  
        arr.append((a,b))  
    arr.sort(key=lambda x:x[0])
    temp = arr[0][1]
    for i in range(1,len(arr)):
        if arr[i][1]<temp:
            result += 1
            temp = arr[i][1]
    print(result)
            