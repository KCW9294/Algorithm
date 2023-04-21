N = int(input())
k = list(map(int, input().split()))
smallest = k[0]
for i in k:
    if i < smallest:
        smallest = i
big = k[0]
for i in k:
    if i > big:
        big = i
print(smallest, big)