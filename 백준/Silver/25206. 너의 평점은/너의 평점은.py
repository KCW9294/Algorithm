lst = [input().split() for _ in range(20)]
sum=0
total=0
for i in range(20):
    if lst[i][2]=='A+':
        lst[i][2]=lst[i][2].replace('A+','4.5')
    elif lst[i][2]=='A0':
        lst[i][2]=lst[i][2].replace('A0','4.0')
    elif lst[i][2]=='B+':
        lst[i][2]=lst[i][2].replace('B+','3.5')
    elif lst[i][2]=='B0':
        lst[i][2]=lst[i][2].replace('B0','3.0')
    elif lst[i][2]=='C+':
        lst[i][2]=lst[i][2].replace('C+','2.5')
    elif lst[i][2]=='C0':
        lst[i][2]=lst[i][2].replace('C0','2.0')
    elif lst[i][2]=='D+':
        lst[i][2]=lst[i][2].replace('D+','1.5')
    elif lst[i][2]=='D0':
        lst[i][2]=lst[i][2].replace('D0','1.0')
    elif lst[i][2]=='F':
        lst[i][2]=lst[i][2].replace('F','0.0')
for i in range(20):
    if lst[i][2]!='P':
        sum = sum + float(lst[i][1])*float(lst[i][2])
        total = total + float(lst[i][1])
print(sum/total)