def solution(arr):
    answer = [0,0]
    length = len(arr[0])

    def quard(x,y,length):
        num = arr[x][y]
        for i in range(x,x+length):
            for j in range(y,y+length):
                if num!=arr[i][j]:
                    quard(x,y+length//2,length//2)
                    quard(x+length//2,y,length//2)
                    quard(x+length//2,y+length//2,length//2)
                    quard(x,y,length//2)
                    return
                
        answer[num] += 1
    
    quard(0,0,length)
            
    return answer