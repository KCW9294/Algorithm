H, M = map(int, input().split())
time = int(input())
result = H*60+M
result+=time
if (result//60)>=24:
    H = result//60-24
else:
    H = result//60
print(H,result%60)