import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
M = int(input())
temp = list(map(int,input().split()))
dic = {}
for i in range(len(lst)):
    dic[lst[i]] = 0 

for i in temp:
    if i in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')