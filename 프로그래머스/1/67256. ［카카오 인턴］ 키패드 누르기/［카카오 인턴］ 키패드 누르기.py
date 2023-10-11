def solution(numbers, hand):
    phone = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
    left = (3,0)
    right = (3,2)
    answer = ''
    for i in numbers:
        if i in [1,4,7]:
            left = phone[i]
            answer += 'L'
        elif i in [3,6,9]:
            right = phone[i]
            answer += 'R'
        else:
            x,y = phone[i][0],phone[i][1]
            left_d = abs(x-left[0])+abs(y-left[1])
            right_d = abs(x-right[0])+abs(y-right[1])
            if left_d > right_d:
                right = phone[i]
                answer += 'R'
            elif right_d > left_d:
                left = phone[i]
                answer += 'L'
            else:
                if hand == 'right':
                    right = phone[i]
                    answer += 'R'
                else:
                    left = phone[i]
                    answer += 'L'
    return answer