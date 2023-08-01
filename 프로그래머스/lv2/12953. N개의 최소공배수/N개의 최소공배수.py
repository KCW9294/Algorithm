# 최대공약수(GCD)를 구하는 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 최소공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# n개의 수들의 최소공배수를 구하는 함수
def solution(arr):
    answer = 1
    for num in arr:
        answer = lcm(answer, num)
    return answer