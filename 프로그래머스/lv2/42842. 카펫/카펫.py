def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i==0:
            if (i+2)*(yellow//i+2)==brown+yellow:
                answer.append(i+2)
                answer.append(yellow//i+2)
    answer.sort(reverse=True)
    return answer