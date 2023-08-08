def solution(numbers):
    answer = [0]*len(numbers)
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i] >= numbers[j] and j != len(numbers)-1:
                continue
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
            if numbers[j] == numbers[-1]:
                answer[i] = -1
                
    return answer
