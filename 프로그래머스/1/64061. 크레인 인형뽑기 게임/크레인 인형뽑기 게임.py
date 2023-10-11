def solution(board, moves):
    answer = 0
    baguni = []
    temp = [[] for _ in range(len(board))]
    for i in board:
        for j in range(len(i)):
            if i[j]!=0:
                temp[j].append(i[j])
    for i in moves:
        if temp[i-1]:
            baguni.append(temp[i-1].pop(0))
            if len(baguni)>=2 and baguni[-1]==baguni[-2]:
                baguni.pop()
                baguni.pop()
                answer += 2
    return answer