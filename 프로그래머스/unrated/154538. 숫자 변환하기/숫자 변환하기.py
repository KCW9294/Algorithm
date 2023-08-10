def solution(x, y, n):
    answer = 0
    temp = set()
    temp.add(x)
    while temp:
        if y in temp:
            return answer
        lst = set()
        for i in temp:
            if i+n <= y:
                lst.add(i+n)
            if i*2 <= y:
                lst.add(i*2)
            if i*3 <= y:
                lst.add(i*3)
        temp = lst
        answer+=1

    return -1