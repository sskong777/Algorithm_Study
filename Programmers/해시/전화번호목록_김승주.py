#  접두어인 경우가 있으면 false / 아니면 true
def solution(phone_book):
    phone_book.sort() # 문자열 정렬 
    for i in range(len(phone_book)-1):
        if phone_book[i][::] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True