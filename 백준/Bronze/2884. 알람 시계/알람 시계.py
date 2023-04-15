H, M = map(int, input().split())
if (M<45) & (H==0):
    H=23
    M=M+15
elif (M<45) & (H!=0):
    H=H-1
    M=M+15
elif (M>=45):
    H=H
    M=M-45
print(H,M)