N = input().split()
a = N[0][2]+N[0][1]+N[0][0]
b = N[1][2]+N[1][1]+N[1][0]
if int(a)>int(b):
    print(a)
else:
    print(b)