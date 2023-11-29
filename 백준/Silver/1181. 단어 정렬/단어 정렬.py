N = int(input())
lst = []

for i in range(N):
    temp = input()
    lst.append((temp,len(temp)))
lst = set(lst)
lst = list(lst)
lst.sort(key=lambda x:(x[1],x[0]))

for word, _ in lst:
    print(word)