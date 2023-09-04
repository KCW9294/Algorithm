def solution(rows, columns, queries):
    answer = []
    matrix = [[0]*(columns+1) for _ in range(rows+1)]
    num = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            matrix[i][j] = num
            num += 1
    for i in queries:
        row = i[2]-i[0]
        column = i[3]-i[1]
        nx,ny = i[0],i[1]
        lst = []
        temp = matrix[nx][ny]
        for k in range(1,(row+1)*(column+1)-(row-1)*(column-1)+1):
            if k<=row:
                num = matrix[nx+1][ny]
                matrix[nx][ny] = num
                lst.append(matrix[nx][ny])
                nx = nx+1
            elif row<k<=column+row:
                num = matrix[nx][ny+1]
                matrix[nx][ny] = num
                lst.append(matrix[nx][ny])
                ny = ny+1
            elif column+row<k<=2*row+column:
                num = matrix[nx-1][ny]
                matrix[nx][ny] = num
                lst.append(matrix[nx][ny])
                nx = nx-1
            elif 2*row+column<k<=2*column+2*row:
                num = matrix[nx][ny-1]
                matrix[nx][ny] = num
                lst.append(matrix[nx][ny])
                ny = ny-1
        matrix[nx][ny+1] = temp
        lst.append(temp)
        answer.append(min(lst))
        
    return answer