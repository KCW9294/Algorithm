def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1,-1]:
                    continue
                if board[j][k] == board[k][i] == 1:
                    board[j][i] = 1
                    board[i][j] = board[k][j] = board[i][k] = -1
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer