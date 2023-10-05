import sys

raiser = input()
raiser = raiser.replace('()','R')

temp = 0
result = 0
for i in raiser:
    if i=='(':
        temp += 1
    elif i==')':
        result += 1
        temp -= 1
    else:
        result += temp

print(result)