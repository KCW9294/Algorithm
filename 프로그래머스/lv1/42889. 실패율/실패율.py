def solution(N, stages):
    failure_rates = []
    total_players = len(stages)
    
    for stage in range(1, N+1):
        if total_players == 0:
            failure_rate = 0
        else:
            players_on_stage = stages.count(stage)
            failure_rate = players_on_stage / total_players
        failure_rates.append((stage, failure_rate))
        total_players -= players_on_stage
    
    failure_rates.sort(key=lambda x: (-x[1], x[0]))  # 실패율 내림차순, 스테이지 번호 오름차순으로 정렬
    
    answer = [stage for stage, _ in failure_rates]
    return answer
