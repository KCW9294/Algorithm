def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = -1
        break_go = False
        
        for i in range(len(tree)): 
            for j in range(len(skill)):
                if tree[i] == skill[j]:
                    temp += 1
                    if temp != j:
                        break_go = True
                        break
            if break_go == True:
                break
        if break_go == False:
            answer += 1

                            
                
    return answer