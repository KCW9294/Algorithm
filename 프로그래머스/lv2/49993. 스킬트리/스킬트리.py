def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        idx = 0
        possible = True

        for i in tree: 
            if i in skill:
                if i != skill[idx]:
                    possible = False
                    break
                else:
                    idx += 1
        
        if possible:
            answer += 1
                            
                
    return answer