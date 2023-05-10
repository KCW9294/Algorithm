N = int(input())
lst = [input() for _ in range(N)]
cnt=0
for i in range(len(lst)):
    for j in range(len(lst[i])-1):
        if lst[i][j]!=lst[i][j+1]:
            new = lst[i][j+1:]
            if new.count(lst[i][j])>0:
                cnt+=1
                break
print(N-cnt)