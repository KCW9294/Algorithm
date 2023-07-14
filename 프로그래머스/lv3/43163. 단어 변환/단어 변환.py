from collections import deque
def solution(begin, target, words):
    visited = [0]*len(words)
    if target not in words:
        return 0
    else:
        answer = dfs(begin, target, words, visited)
        return answer
    
        
def dfs(begin, target, words, visited):
    deq = deque()
    deq.append([begin,0])
    while deq:
        word, cnt = deq.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            count = 0
            if visited[i]==1:
                continue
            for j in range(len(word)):
                if word[j]!=words[i][j]:
                    count += 1
            if count==1:
                temp_cnt = cnt+1
                deq.append([words[i],temp_cnt])
                visited[i]=1
                