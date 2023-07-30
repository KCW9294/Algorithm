def solution(s):
    new_s = ""
    del_zero = 0
    count = 0
    while s != "1":
        for i in s:
            if i == "1":
                new_s += i
            else:
                del_zero += 1
        count += 1
        s = bin(len(new_s))[2:]
        new_s = ""
    
    answer = [count, del_zero]
    return answer