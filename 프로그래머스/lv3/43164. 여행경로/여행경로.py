from collections import deque
def solution(tickets):
    deq = deque()
    deq.append(["ICN",["ICN"],[]])
    answer = []
    while deq:
        start, line, visited = deq.popleft()
        if len(line)==len(tickets)+1:
            answer.append(line)
        for i in range(len(tickets)):
            if tickets[i][0]==start and i not in visited:
                deq.append([tickets[i][1],line+[tickets[i][1]],visited+[i]])
    answer.sort()
    return answer[0]
        
                           
    