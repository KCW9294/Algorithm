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
