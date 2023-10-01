def check(place):
    # 'P'인 것의 좌표만 저장
    dist = [(x,y) for x in range(5) for y in range(5) if place[x][y]=='P']
    
    # 좌표 간 거리 계산
    for x,y in dist:
        for x2,y2 in dist:
            temp = abs(x-x2) + abs(y-y2) #맨해튼 거리
            if temp==0 or temp>2:
                continue
            elif temp==1:
                return 0
            elif x==x2 and place[x][(y+y2)//2]!='X': #행 같고 두 사람 사이 파티션이 없는 경우
                return 0
            elif y==y2 and place[(x+x2)//2][y]!='X': #열 같고 두 사람 사이 파티션이 없는 경우
                return 0
            elif x!=x2 and y!=y2: # 대각선에 있는 경우
                if place[x][y2]!='X' or place[x2][y]!='X': # 사이에 파티션이 둘다 없는 경우
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer
                
