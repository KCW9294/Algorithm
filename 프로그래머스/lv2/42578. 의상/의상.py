def solution(clothes):
    hashlist = {}
    answer = 1
    for cloth in clothes:
        hashlist[hash(cloth[1])] = 0
        hashkey = hashlist.keys()
    for cloth in clothes:
        for j in hashkey:
            if hash(cloth[1])==j:
                hashlist[hash(cloth[1])] += 1
    result = list(hashlist.values())
    for i in result:
        answer *= i+1
    return answer-1