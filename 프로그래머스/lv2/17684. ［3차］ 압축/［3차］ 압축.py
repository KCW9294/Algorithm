def solution(msg):
    answer = []
    dic = {chr(i+64): i for i in range(1,27)} # 딕셔너리 형태로 
    i = 0
    cnt = 27 # 새로운 단어 색인 번호 시작점
    s = ''
    
    while i < len(msg): 
        s += msg[i]
        if s in dic:
            i += 1
            continue
        else:
            dic[s] = cnt
            cnt += 1
            answer.append(dic[s[:-1]]) # 마지막 글자를 제외한 나머지는 색인 번호 출력
            s = ''
        
    answer.append(dic[s])
    
    return answer