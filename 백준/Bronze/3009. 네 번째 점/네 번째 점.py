lst = [list(map(int, input().split())) for _ in range(3)]
a=0
b=0
if lst[0][0]==lst[1][0]:
    a=lst[2][0]
elif lst[0][0]==lst[2][0]:
    a=lst[1][0]
else:
    a=lst[0][0]
    
if lst[0][1]==lst[1][1]:
    b=lst[2][1]
elif lst[0][1]==lst[2][1]:
    b=lst[1][1]
else:
    b=lst[0][1]

print(a,b)