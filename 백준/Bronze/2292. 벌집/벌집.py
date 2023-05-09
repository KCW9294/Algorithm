n = int(input())
i = 0
cnt = 0
t = 1
while True:
    if n == 1:
        print(1)
        break
    else:
        if n > t + (6 * i):
            t = t + (6 * i)
            i += 1
            cnt += 1
        else:
            print(cnt+1)
            break