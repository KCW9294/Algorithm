def solution(n, k):
    answer = 0
    num = change(n, k)
    temp = ""
    for i in range(len(num)):
        if int(num[i])!=0:
            temp += num[i]
        if (int(num[i])==0 and temp) or (temp and i==len(num)-1):
            temp = int(temp)
            if temp == 1:
                pass
            else:
                temp_temp = 0
                for k in range(2,int(temp**0.5+1)):
                    if temp%k==0:
                        temp_temp += 1
                if temp_temp == 0:
                    answer += 1
            temp = ""
    
    return answer

def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    