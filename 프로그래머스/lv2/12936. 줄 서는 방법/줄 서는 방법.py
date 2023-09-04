import math
def solution(n, k):
    lst = []
    answer = []
    k = k-1
    for i in range(1,n+1):
        lst.append(i)
    while n!=0:
        idx = k//math.factorial(n-1)
        k = k%math.factorial(n-1)
        answer.append(lst.pop(idx))
        n -= 1

    return answer