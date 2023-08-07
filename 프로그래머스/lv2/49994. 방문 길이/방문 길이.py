def solution(dirs):
    x,y = 0,0
    go = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    visited = set()
    answer = 0
    
    for i in dirs:
        dx, dy = go[i]
        ux, uy = x + dx, y + dy
        if -5 <= ux <= 5 and -5 <= uy <= 5:
            path = ((x, y), (ux, uy))
            reverse_path = ((ux, uy), (x, y))
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                answer += 1
        else:
            continue
        x, y = ux, uy
    
    return answer
            