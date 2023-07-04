def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] < phone_book[i+1]:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
    return True

# 나의 풀이로는 점수가 85밖에 안되어서 풀이 참고
# str형태의 리스트를 sort하면 0,1,123,1234,1237 이런식으로 정렬됨 ★

#아래는 나의 풀이
def solution(phone_book):
    lst = list(map(int,phone_book))
    lst.sort()
    lst = list(map(str,lst))

    for i in lst:
        for j in lst:
            if i == j[:len(i)] and i!=j:
                return False
    return True
