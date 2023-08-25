def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = [i,j]
                break
                
    for i in routes:
        x,y = i.split(" ")
        if x == 'E':
            temp = [0,int(y)]
            if 0<=start[0]+temp[0]<len(park) and 0<=start[1]+temp[1]<len(park[0]):
                for k in range(1,int(y)+1):
                    if park[start[0]][start[1]+k]=='X':
                        break
                    if k == int(y):
                        start[0]+=temp[0]
                        start[1]+=temp[1]
        elif x == 'W':
            temp = [0,-int(y)]
            if 0<=start[0]+temp[0]<len(park) and 0<=start[1]+temp[1]<len(park[0]):
                for k in range(1,int(y)+1):
                    if park[start[0]][start[1]-k]=='X':
                        break
                    if k == int(y):
                        start[0]+=temp[0]
                        start[1]+=temp[1]
        elif x == 'N':
            temp = [-int(y),0]
            if 0<=start[0]+temp[0]<len(park) and 0<=start[1]+temp[1]<len(park[0]):
                for k in range(1,int(y)+1):
                    if park[start[0]-k][start[1]]=='X':
                        break
                    if k == int(y):
                        start[0]+=temp[0]
                        start[1]+=temp[1]
        else:
            temp = [int(y),0]
            if 0<=start[0]+temp[0]<len(park) and 0<=start[1]+temp[1]<len(park[0]):
                for k in range(1,int(y)+1):
                    if park[start[0]+k][start[1]]=='X':
                        break
                    if k == int(y):
                        start[0]+=temp[0]
                        start[1]+=temp[1]

    
    return start