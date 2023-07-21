def solution(progresses, speeds):
    bepo = []
    answer = []
    possible = 0
    for i in range(len(progresses)):
        if ((100-progresses[i])%speeds[i]) != 0:
            bepo.append((100-progresses[i])//speeds[i]+1)
        else:
            bepo.append((100-progresses[i])//speeds[i])
    
    num = bepo[0]
    for i in range(len(bepo)):
        possible += 1
        if i==len(bepo)-1:
            answer.append(possible)
            break
        if num < bepo[i+1]:
            answer.append(possible)
            num = bepo[i+1]
            possible = 0
    return answer