def solution(phone_book):
    book = {}
    for i in phone_book:
        book[i] = 1

    for phone in phone_book:
        front = ""
        for num in phone:
            front += num

            # book이 hashmap
            if front in book and front != phone:
                return False

    return True