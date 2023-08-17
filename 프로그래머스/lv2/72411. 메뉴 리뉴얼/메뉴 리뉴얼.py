from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        com_dic = {}
        coms = []
        for order in orders:
            coms.extend(list(combinations(sorted(order),i)))
            
        for com in coms:
            temp = ''.join(com)
            if temp in com_dic:
                com_dic[temp] += 1
            else:
                com_dic[temp] = 1
        
        for com in com_dic:
            if com_dic[com] == max([com_dic[com] for com in com_dic]):
                if com_dic[com] >1:
                    answer.append(com)

    return sorted(answer)