def hanoi(n, start, end, to):
    if n == 1:
        return [(start, end)]
    else:
        moves = hanoi(n - 1, start, to, end)
        moves.append((start, end))
        moves += hanoi(n - 1, to, end, start)
        return moves

def solution(n):
    return hanoi(n, 1, 3, 2)


    