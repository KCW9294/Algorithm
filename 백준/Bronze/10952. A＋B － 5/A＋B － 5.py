temp1 = []
temp2 = []
while(True):
    A,B = map(int, input().split())
    if (A==0) & (B==0):
        break
    temp1.append(A)
    temp2.append(B)
for i in range(len(temp1)):
    print(temp1[i]+temp2[i])
  