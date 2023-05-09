A, B, V = map(int, input().split())

time = 0
cnt = 0

a=V-A
b=A-B
if a%b==0:
    print(a//b+1)
else:
    print(a//b+1+1)