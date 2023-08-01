def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        l = min(len(phone_book[i]), len(phone_book[i+1]))
        if l == len(phone_book[i]):
            if phone_book[i] == phone_book[i+1][:l]:
                answer = False
        else:
            if phone_book[i+1] == phone_book[i][:l]:
                answer = False
    return answer