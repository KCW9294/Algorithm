def solution(n):
    temp = bin(n)[2:].count("1")
    while True:
        n += 1
        if bin(n)[2:].count("1") == temp:
            answer = int(bin(n), 2)
            break

    return answer