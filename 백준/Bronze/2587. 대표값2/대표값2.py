lst = []
for i in range(5):
    lst.append(int(input()))
    
print(sum(lst)//5)
lst.sort()
print(lst[2])