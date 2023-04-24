W = []
length = []
for _ in range(5):
    s = input()
    W.append(s)
    length.append(len(s))
    
result = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result += W[j][i]
print(result)
