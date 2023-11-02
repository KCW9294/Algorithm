N = int(input())
poong = list(map(int,input().split()))
index = [i for i in range(1,N+1)]
answer = []
start = 0

while poong:
    answer.append(str(index.pop(start)))
    temp = poong.pop(start)
    if not poong:
        break
    if temp<0:
        start = (start+temp)%len(poong)
    else:
        start = (start+temp-1)%len(poong)
        
print(' '.join(answer))
