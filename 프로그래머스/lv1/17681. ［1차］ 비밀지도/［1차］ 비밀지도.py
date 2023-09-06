def solution(n, arr1, arr2):
    answer = ['']*n
    map1 = ['']*n
    map2 = ['']*n
    for i in range(len(arr1)):
        if len(bin(arr1[i])[2:])<n:
            map1[i] = (n-len(bin(arr1[i])[2:]))*'0'+bin(arr1[i])[2:]
        else:
            map1[i] = bin(arr1[i])[2:]
            
    for i in range(len(arr2)):
        if len(bin(arr2[i])[2:])<n:
            map2[i] = (n-len(bin(arr2[i])[2:]))*'0'+bin(arr2[i])[2:]
        else:
            map2[i] = bin(arr2[i])[2:]
            
    for i in range(n):
        for j in range(n):
            if map1[i][j]=='1' or map2[i][j]=='1':
                answer[i] += '#'
            else:
                answer[i] += ' '
            
    return answer