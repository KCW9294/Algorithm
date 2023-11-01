yose = list(map(int,input().split()))

lst = [i for i in range(1,yose[0]+1)]
temp = 0

answer = []
while lst:
    temp += yose[1]-1
    if temp>=len(lst):
        temp %= len(lst)
    answer.append(str(lst.pop(temp)))
    
print("<", ", ".join(answer), ">", sep="")
    