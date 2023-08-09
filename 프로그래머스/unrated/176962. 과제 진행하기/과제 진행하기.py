def solution(plans):
    answer, new_plans = {}, []
    
    # new_plan에다가 튜플 형식으로 넣기 위한 for문
    for plan in plans:
        # (이름, start를 분으로 환산한 값, playtime) 형식으로 넣어준다.
        new_plans.append((plan[0],int(plan[1][:2])*60+int(plan[1][3:]),int(plan[2])))
        # answer 딕셔너리에 key값으로 이름, value값으로 start를 분으로 환산한 값을 넣어준다.
        answer[plan[0]] = int(plan[1][:2])*60+int(plan[1][3:])
        
    # start를 분으로 환산한 값을 기준으로 정렬한다.
    new_plans.sort(key=lambda x:x[1])
    
    # 시작시간이 짧은 과제부터 차례대로 for문을 돈다.
    for i in range(len(new_plans)):
        # answer[name]에 playtime을 더해준다.
        answer[new_plans[i][0]] += new_plans[i][2]
        # 선택된 과제 이후의 과제들을 for문을 돌면서 answer[name]의 값보다 작을시 이후 과제들의 playtime을 계속해서 더해준다. 
        for j in range(i+1,len(new_plans)):
            if answer[new_plans[i][0]]>answer[new_plans[j][0]]:
                answer[new_plans[i][0]] += new_plans[j][2]
                                                  
    # 결과적으로 answer에는 과제 이름별로 과제가 끝나는 시간이 기록되어있는데 이 값을 정렬해준다.
    answer = sorted(answer.items(), key=lambda x: x[1])
    for i in range(len(answer)):
        answer[i] = answer[i][0]
    return answer
