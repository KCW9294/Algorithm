def solution(m, musicinfos):
    answer = []
    m=m.replace('C#','c')
    m=m.replace('D#','d')
    m=m.replace('F#','f')
    m=m.replace('G#','g')
    m=m.replace('A#','a')
    
    print(m)
    
    for i in musicinfos:
        temp = i.split(',')
        idx = 0
        code = []
        music = ''
        temp[3]=temp[3].replace('C#','c')
        temp[3]=temp[3].replace('D#','d')
        temp[3]=temp[3].replace('F#','f')
        temp[3]=temp[3].replace('G#','g')
        temp[3]=temp[3].replace('A#','a')
        
        for i in range(60*(int(temp[1][:2])-int(temp[0][:2]))+(int(temp[1][3:])-int(temp[0][3:]))):
            music += temp[3][i%len(temp[3])]
        if m in music:
            answer.append((temp[2],60*(int(temp[1][:2])-int(temp[0][:2]))+(int(temp[1][3:])-int(temp[0][3:]))))
    if answer:
        answer.sort(key=lambda x:x[1],reverse=True)
        return answer[0][0]
    else:
        return "(None)"