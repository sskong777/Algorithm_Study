def solution(phone_book):
    answer = True

    phone = phone_book
    dic = dict()

    for d in phone_book:
        dic[d] = d

    for i in range(len(phone)):
        tmp = ''
        for j in phone[i]:
            tmp += j
            if tmp in dic and tmp != phone[i]:
                return False

    return answer