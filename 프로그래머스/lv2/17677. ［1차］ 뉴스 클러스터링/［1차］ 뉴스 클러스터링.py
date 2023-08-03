def solution(str1, str2):
    new_str1 = []
    new_str2 = []
    
    for i in range(0,len(str1)-1):
        temp = str1[i:i+2].lower()
        if temp.isalpha():
            new_str1.append(temp)
    for i in range(0,len(str2)-1):
        temp = str2[i:i+2].lower()
        if temp.isalpha():
            new_str2.append(temp)       
    
    common = 0
    
    for m in set(new_str1):
        if new_str1.count(m)>0 and new_str2.count(m)>0:
            common += min(new_str1.count(m), new_str2.count(m))
    
    allresource = 0

    for m in set(new_str1):
        if new_str1.count(m)>0 and new_str2.count(m)>0:
            allresource += max(new_str1.count(m), new_str2.count(m))
    
    for u in new_str1:
        if u not in new_str2:
            allresource += 1
    
    for u in new_str2:
        if u not in new_str1:
            allresource += 1
            
    if common == 0 and allresource != 0:
        return 0
    
    if common == 0 and allresource == 0:
        return 65536
    
    answer = int(65536*(common/allresource))
    return answer