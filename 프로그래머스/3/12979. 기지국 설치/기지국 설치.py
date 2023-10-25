import math
def solution(n, stations, w):
    answer = 0
    if len(stations)==1:
        temp = stations[0]-w-1
        if temp>0:
            answer += math.ceil(temp/(w*2+1))
        temp = n-stations[0]-w
        if temp>0:
            answer += math.ceil(temp/(w*2+1))
    else:
        for i in range(len(stations)):
            if i==0:
                temp = stations[i]-w-1
                if temp>0:
                    answer += math.ceil(temp/(w*2+1))
            elif i==len(stations)-1:
                temp = n-stations[i]-w
                if temp>0:
                    answer += math.ceil(temp/(w*2+1))
                temp = stations[i]-stations[i-1]-w*2-1
                if temp>0:
                    answer += math.ceil(temp/(w*2+1))
            else:
                temp = stations[i]-stations[i-1]-w*2-1
                if temp>0:
                    answer += math.ceil(temp/(w*2+1))
            
    return answer