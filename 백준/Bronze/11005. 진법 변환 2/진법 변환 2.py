a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b,k = map(int, input().split())
results = []
while True:
    results.append(b%k)
    b//=k
    if k>b:
        results.append(b)
        break
results.reverse()
q = [a[x] for x in results]
if q[0]=='0':
    q=q[1:]

print(''.join(q))