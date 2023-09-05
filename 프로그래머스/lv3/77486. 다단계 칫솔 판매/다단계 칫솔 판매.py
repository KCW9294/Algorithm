def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}
    piramid = {}
    for i in enroll:
        dic[i] = 0
    for i in enroll:
        piramid[i] = ""
    for i in range(len(enroll)):
        if referral[i] != "-":
            piramid[enroll[i]]=referral[i]
            
    def bfs(name,income):
        if piramid[name] and income>=10:
            dic[name]+=income-int(income*0.1)
            bfs(piramid[name],int(income*0.1))
        else:
            dic[name]+=income-int(income*0.1)
    
    for i in range(len(seller)):
        income = 100*amount[i]
        if piramid[seller[i]] and income>=10:
            dic[seller[i]]+=income-int(income*0.1)
            bfs(piramid[seller[i]],int(income*0.1))
        else:
            dic[seller[i]]+=income-int(income*0.1)
            
    for i in dic:
        answer.append(dic[i])
    
    return answer
