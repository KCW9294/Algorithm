def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            zero += 1
    if cnt+zero==6:
        answer.append(1)
    elif cnt+zero==5:
        answer.append(2)
    elif cnt+zero==4:
        answer.append(3)
    elif cnt+zero==3:
        answer.append(4)
    elif cnt+zero==2:
        answer.append(5)
    else:
        answer.append(6)
    if cnt==6:
        answer.append(1)
    elif cnt==5:
        answer.append(2)
    elif cnt==4:
        answer.append(3)
    elif cnt==3:
        answer.append(4)
    elif cnt==2:
        answer.append(5)
    else:
        answer.append(6)
        
    return answer