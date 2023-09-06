def solution(book_time):
    answer = 0
    temp = []
    result = []
    for i in range(len(book_time)):
        temp.append((60*int(book_time[i][0][:2])+int(book_time[i][0][3:]),'start'))
        temp.append((60*int(book_time[i][1][:2])+int(book_time[i][1][3:])+10,'end'))
    
    temp.sort()
    cnt = 0
    for i in temp:
        if i[1]=='start':
            cnt += 1
        else:
            cnt -= 1
        result.append(max(answer,cnt))

    return max(result)