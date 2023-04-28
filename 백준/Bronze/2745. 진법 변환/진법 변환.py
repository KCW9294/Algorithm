import sys
word,num = input().split()
num = int(num)
word = list(word)
sum = 0
for i in range(len(word),0,-1):
    if ord(word[len(word)-i]) >= 65 and ord(word[len(word)-i]) <= 90:
        sum += (ord(word[len(word)-i]) - ord('A') + 10)*(num**(i-1))
    else:
        word[len(word)-i] = int(word[len(word)-i])
        sum += word[len(word)-i]*(num**(i-1))
print(sum)