'''def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[j].startswith(phone_book[i]):
                return False

    return True

phone_book =["123","456","789"]

print(len(phone_book))

print(solution(phone_book))'''

def solution(phone_book):
    phone_book.sort()
    # 전화번호를 정렬하여 접두어인지 판별하기 위해 비교할 때 앞뒤 번호끼리 비교

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
