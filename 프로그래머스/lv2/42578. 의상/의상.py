# def solution(clothes):
#     hashlist = {}
#     answer = 1
#     for cloth in clothes:
#         hashlist[hash(cloth[1])] = 0
#     hashkey = hashlist.keys()
#     print(hashkey)
#     for cloth in clothes:
#         for j in hashkey:
#             if hash(cloth[1])==j:
#                 hashlist[hash(cloth[1])] += 1
#     result = list(hashlist.values())
#     for i in result:
#         answer *= i+1
#     return answer-1

def solution(clothes):
    dic = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1
            
    for i in dic:
        answer *= dic[i]+1
        
    return answer-1