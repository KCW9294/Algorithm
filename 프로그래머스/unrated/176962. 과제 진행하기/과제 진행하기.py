def solution(plans):
    answer = {}
    new_plans = []
    temp = []
    for plan in plans:
        new_plans.append((plan[0],int(plan[1][:2])*60+int(plan[1][3:]),int(plan[2])))
    new_plans.sort(key=lambda x:x[1])
    
    for plan in new_plans:
        answer[plan[0]] = plan[1]
    
    for i in range(len(new_plans)):
        answer[new_plans[i][0]] += new_plans[i][2]
        for j in range(i+1,len(new_plans)):
            if answer[new_plans[i][0]]>answer[new_plans[j][0]]:
                answer[new_plans[i][0]] += new_plans[j][2]
                                                  
    answer = sorted(answer.items(), key=lambda x: x[1])
    for i in answer:
        temp.append(i[0])
    return temp