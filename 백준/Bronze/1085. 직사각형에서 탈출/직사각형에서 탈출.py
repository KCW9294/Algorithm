x,y,w,h = map(int,input().split())
k = abs(x-w)
q = abs(h-y)

min=0
min2=0
if x>y:
    min2=y
else:
    min2=x
    
if k>q:
    min=q
else:
    min=k
    
if min>min2:
    print(min2)
else:
    print(min)
    