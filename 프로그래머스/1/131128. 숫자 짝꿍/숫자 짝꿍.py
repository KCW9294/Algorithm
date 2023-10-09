def solution(X, Y):
    answer = ''
    lst = [0]*10
    # X의 각자리의 숫자가 Y에서 몇개 있는지 파악하여 lst에 저장
    for i in range(10):
        lst[int(i)] = min(X.count(str(i)),Y.count(str(i)))
    # 큰 수부터 각 숫자의 갯수만큼 곱하여 answer에 더해줌
    for i in range(len(lst)-1,-1,-1):
        answer += lst[i]*str(i)
    # 문자가 비어있을시 -1
    if answer == '':
        answer = '-1'
    # 00과 같은 경우를 처리하기 위해 int->str과정 추가
    elif len(answer)==answer.count('0'):
        answer = '0'
    return answer