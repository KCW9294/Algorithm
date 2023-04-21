s = input()
lst = [-1] * 26 # 알파벳 개수(26)만큼 리스트 생성 후 -1로 초기화

for i in range(len(s)):
    index = ord(s[i]) - ord('a') # 알파벳이 리스트에서 몇 번째 인덱스에 해당하는지 계산
    if lst[index] == -1:
        lst[index] = i # 처음 등장한 위치 저장
for i in range(len(lst)):
    print(lst[i],end=' ')