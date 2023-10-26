# from collections import deque
# def solution(begin, target, words):
#     visited = [0]*len(words)
#     if target not in words:
#         return 0
#     else:
#         answer = bfs(begin, target, words, visited)
#         return answer
    
# def bfs(begin, target, words, visited):
#     deq = deque()
#     deq.append((begin,0))
#     while deq:
#         word,cnt = deq.popleft()
#         if word == target:
#             return cnt
#         else:
#             for i in range(len(words)):
#                 if visited[i] == 0:
#                     temp = 0
#                     for j in range(len(word)):
#                         if word[j] != words[i][j]:
#                             temp += 1
#                     if temp == 1:
#                         deq.append((words[i],cnt+1))
#                         visited[i] = 1
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

                        
from collections import deque
def solution(begin, target, words):
    deq = deque()
    deq.append([begin])
    while deq:
        temp = deq.popleft()
        if temp[-1]==target:
            return len(temp)-1
        for word in words:
            if word not in temp:
                cnt = 0
                for i in range(len(word)):
                    if word[i]==temp[-1][i]:
                        cnt += 1
                if cnt==len(word)-1:
                    deq.append(temp+[word])
    return 0
                    
    