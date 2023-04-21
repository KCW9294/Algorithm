num2 = ['A','B','C']
num3 = ['D','E','F']
num4 = ['G','H','I']
num5 = ['J','K','L']
num6 = ['M','N','O']
num7 = ['P','Q','R','S']
num8 = ['T','U','V']
num9 = ['W','X','Y','Z']
sum=0
phone_num = input()
for i in range(len(phone_num)):
    if phone_num[i] in num2:
        sum+=3
    elif phone_num[i] in num3:
        sum+=4
    elif phone_num[i] in num4:
        sum+=5
    elif phone_num[i] in num5:
        sum+=6
    elif phone_num[i] in num6:
        sum+=7
    elif phone_num[i] in num7:
        sum+=8
    elif phone_num[i] in num8:
        sum+=9
    elif phone_num[i] in num9:
        sum+=10
print(sum)
        