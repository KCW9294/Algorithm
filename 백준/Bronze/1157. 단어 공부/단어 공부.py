s = input()
s = s.upper()
unique = list(set(s))
lst = []
for i in unique:
    lst.append(s.count(i))
max = 0
sol = 0
for i in range(len(lst)):
    if max<lst[i]:
        max=lst[i]
        sol = unique[i]
    
if lst.count(max)>1:
    print('?')
else:
    print(sol)