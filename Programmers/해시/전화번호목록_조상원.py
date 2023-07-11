def solution(phone_book):
    pb = sorted(phone_book)
    for i in range(len(pb)-1):
        curr = pb[i]
        nex = pb[i+1]
        # print(curr, nex)
        if curr == nex[:len(curr)]:
            return False
    return True
        # print(pb[p])
        