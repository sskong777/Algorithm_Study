def solution(phone_book):
    answer = True
    phone_book.sort()
    # print(phone_book)
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            # if phone_book[i] in phone_book[i+1]:
            # 테스트 케이스 하나 통과 못함 -> 접두어 뿐만 아니라 겹치는 번호도 False 처리함
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                return answer
    return answer


# def solution(phone_book):
#     answer = True
#     phone_book.sort(key = lambda x:len(x))

#     for i in range(len(phone_book)):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[j][:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 return answer

#     return answer