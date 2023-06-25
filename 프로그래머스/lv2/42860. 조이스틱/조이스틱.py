def solution(name):
    result = 0
    
    min_length = len(name)-1
    for i in name:
        result += min(ord(i)-ord('A'),ord('Z')-ord(i)+1)
        
    for j in range(len(name)):
        next = j+1
        while next < len(name) and name[next]=='A':
            next += 1
        min_length = min([min_length,j*2+len(name)-next,j+2*(len(name)-next)])

    answer = result + min_length    
    return answer