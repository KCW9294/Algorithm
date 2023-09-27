def solution(arrayA, arrayB):
    answer = [0]
    a = arrayA[0]
    for i in arrayA:
        a = gcd(i,a)
    b = arrayB[0]
    for i in arrayB:
        b = gcd(i,b)
        
    temp = 0
    for i in arrayA:
        if i%b==0:
            temp = 1
            break
    if temp == 0:
        answer.append(b)
    temp = 0
    for i in arrayB:
        if i%a==0:
            temp = 1
            break
    if temp == 0:
        answer.append(a)
        
    return max(answer)
            
def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)