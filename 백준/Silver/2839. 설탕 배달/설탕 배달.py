N=int(input())
M=N
K=N
result = []
cnt=0
cnt2=0
for i in range(M):
    if M<0:
        break
    else:
        M=M-5
        if M<0:
            break
        elif M%5==0:
            result.append(N//5)
            break
        else:
            cnt+=1
            if M%3==0:
                cnt+=M//3
                aaa=cnt
                result.append(aaa)
            else:
                if M==0:
                    result.append(N//5)
                continue
for i in range(K):
    if K<0:
        break
    else:
        K=K-3
        if K<0:
            break
        else:
            cnt2+=1
            if K%5==0:
                cnt2+=K//5
                aaa=cnt2
                result.append(aaa)
            else:
                if K==0:
                    result.append(N//3)
                continue
if len(result)==0:
    print(-1)
else:
    if min(result)==0:
        print(-1)
    else:
        print(min(result))