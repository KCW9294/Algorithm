sentence = input()
boom = input()

temp = []
for i in range(len(sentence)):
    temp.append(sentence[i])
    if temp[-1] == boom[-1]:
        if len(temp)>=len(boom):
            if ''.join(temp[-len(boom):])==boom:
                for i in range(len(boom)):
                    temp.pop()
if temp:
    print(''.join(temp))
else:
    print('FRULA')
        