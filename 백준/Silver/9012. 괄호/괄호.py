N = int(input())

lst = [input() for _ in range(N)]

for PS in lst:
    stack = 0
    go_break = False
    for i in range(len(PS)):
        if PS[i]=='(':
            stack += 1
        else:
            stack -= 1
        if stack<0:
            print('NO')
            go_break = True
            break
    if go_break==True:
        continue
    else:
        if stack==0:
            print('YES')
        else:
            print('NO')