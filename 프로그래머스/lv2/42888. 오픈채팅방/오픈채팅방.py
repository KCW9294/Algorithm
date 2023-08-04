def solution(record):
    answer = []
    temp = {}
    for i in record:
        line = i.split(" ")
        if line[0]=='Enter' or line[0]=='Change':
            temp[line[1]]=line[2]
    
    for k in record:
        line = k.split(" ")
        if line[0]=="Enter":
            answer.append(f"{temp[line[1]]}님이 들어왔습니다.")
        elif line[0]=="Leave":
            answer.append(f"{temp[line[1]]}님이 나갔습니다.")
    
    return answer