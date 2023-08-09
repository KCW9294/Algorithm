def solution(m, n, board):
    answer = 0
    temp = set()
    for i in range(m):
        board[i] = list(board[i])
        
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == []:
                    continue
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    temp.add((i,j))
                    temp.add((i,j+1))
                    temp.add((i+1,j))
                    temp.add((i+1,j+1))

        if temp:
            answer += len(temp)
            for i,j in temp:
                board[i][j] = []
            temp = set()
        else:
            return answer

        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break