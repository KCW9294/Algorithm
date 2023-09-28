def solution(board):
    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]!=0:
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
                if board[i][j]>answer:
                    answer = board[i][j]
    
    for i in board:
        if max(i)>answer:
            answer = max(i)
    
    return answer*answer