lst = [int(input()) for _ in range(9)]
big=lst[0]
idx=0
for i in range(len(lst)):
    if lst[i] > big:
        big = lst[i]
        idx = i
print(big)
print(idx+1)