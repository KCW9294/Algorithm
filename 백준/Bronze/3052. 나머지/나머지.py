lst = [int(input()) for _ in range(10)]
lst = [lst[i]%42 for i in range(len(lst))]
print(len(set(lst)))