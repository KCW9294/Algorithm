def solution(players, callings):
    temp = {}

    for i in range(len(players)):
        temp[players[i]]=i
        
    for i in range(len(callings)):
        idx = temp[callings[i]]
        fp = players[idx-1]
        
        temp[callings[i]] = idx-1
        temp[fp] = idx
        
        players[idx-1] = callings[i]
        players[idx] = fp

    return players