s = input()
if len(s)%2 == 0:
    if s[:len(s)//2]==s[len(s)-1:len(s)//2-1:-1]:
        print(1)
    else:
        print(0)
else:
    if len(s)==1:
        print(1)
    else:
        if s[:len(s)//2+1]==s[len(s)-1:len(s)//2-1:-1]:
            print(1)
        else:
            print(0)