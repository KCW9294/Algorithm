def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        idx = 0
        possible = True

        for s in tree:
            if s in skill:
                if s != skill[idx]:
                    possible = False
                    break
                idx += 1
        
        if possible:
            answer += 1

    return answer