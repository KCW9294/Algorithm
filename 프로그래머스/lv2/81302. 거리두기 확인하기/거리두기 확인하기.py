def check(place):
    dist = [(x,y) for x in range(5) for y in range(5) if place[x][y]=='P']
    
    for x,y in dist:
        for x2,y2 in dist:
            temp = abs(x-x2) + abs(y-y2)
            if temp==0 or temp>2:
                continue
            elif temp==1:
                return 0
            elif x==x2 and place[x][(y+y2)//2]!='X':
                return 0
            elif y==y2 and place[(x+x2)//2][y]!='X':
                return 0
            elif x!=x2 and y!=y2:
                if place[x][y2]!='X' or place[x2][y]!='X':
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer
                
