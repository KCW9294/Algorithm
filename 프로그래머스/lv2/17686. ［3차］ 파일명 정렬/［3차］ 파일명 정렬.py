def solution(files):
    answer = []
    temp = []
    for file in files:
        head, num, tail = '','',''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                num = file[i:]
                
                for j in range(len(num)):
                    if num[j].isdigit()==False:
                        tail = num[j:]
                        num = num[:j]
                        break
                break
        temp.append((head,num,tail))
    
    temp.sort(key=lambda x:(x[0].lower(),int(x[1])))
    # temp = sorted(temp, key=lambda x:(x[0].lower(), int(x[1])))
    
    for k in temp:
        answer.append(k[0]+k[1]+k[2])
    
                
    return answer