N = int(input())
result = 1

def abc(N):
    global result
    if N==0:
        return
    result *= N
    abc(N-1)

if N==0:
    print(1)
else:
    abc(N)
    print(result)
    
    