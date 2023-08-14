def solution(numbers):
    answer = []
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            temp = list(bin(num)[2:])
            if '0' not in temp:
                answer.append(int('10'+''.join(temp[1:]),2))
            else:
                for i in range(len(temp)-1,-1,-1):
                    if temp[i] == '0':
                        temp[i] = '1'
                        temp[i+1] = '0'
                        break
                answer.append(int(''.join(temp),2))
                    

    return answer