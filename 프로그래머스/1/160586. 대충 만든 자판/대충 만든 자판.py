def solution(keymap, targets):
    answer = [0]*len(targets)
    for i in range(len(targets)):
        # targets[i]의 각 알파벳을 뽑아줌
        for j in targets[i]:
            temp = 100
            cnt = 0
            for key in keymap:
                # targets의 알파벳이 keymap에 있는 경우 min을 통해 가장 작은 index를 찾아줌
                if j in key:
                    temp = min(temp,key.index(j)+1)
                else:
                    cnt += 1
                # 어느 key로도 알파벳을 만들지 못하는 경우
                if cnt == len(keymap):
                    temp = -1
            # targets의 문자열을 만들 수 없는 경우 
            if temp==-1:
                answer[i] = -1
                break
            else:
                answer[i] += temp
    return answer