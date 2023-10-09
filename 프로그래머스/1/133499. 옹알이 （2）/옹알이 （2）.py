def solution(babbling):
    answer = 0
    # babbling의 단어 중 발음들을 1,2,3,4로 바꿔줌
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace('aya','1')
        babbling[i] = babbling[i].replace('ye','2')
        babbling[i] = babbling[i].replace('woo','3')
        babbling[i] = babbling[i].replace('ma','4')
        
    # isdigit()를 활용하여 숫자가 아닌경우 발음 할 수 없는 것으로 간주
    for word in babbling:
        temp = ''
        for i in range(len(word)):
            # 연속으로 발음인지 확인
            if temp==word[i]:
                break
            # 숫자가 아닌 경우 break
            if not word[i].isdigit():
                break
            # 연속으로 발음한 것을 처리하기 위해 temp에 저장
            else:
                temp = word[i]
            # 마지막까지 무사히 통과되면 answer += 1
            if i==len(word)-1:
                answer += 1
    
    return answer