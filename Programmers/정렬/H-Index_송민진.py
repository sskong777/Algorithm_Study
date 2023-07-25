# 시도 1
# import math
#
# def solution(citations):
#     citations.sort()
#     n = len(citations)
#     if n == 1:
#         return citations[0]
#
#     mid = math.ceil(n / 2)
#     return min(mid, citations[mid-1])

# 시도 2
# import math
#
# def solution(citations):
#     citations.sort()
#     if len(citations) == 1:
#         return min(citations[0], 1)
#     mid = math.floor(len(citations) / 2)
#     tmp = citations[mid]
#     # print(mid, tmp)
#     if citations[0] > mid:
#         return len(citations)
#     if tmp > mid:
#         return mid
#     return tmp

# 시도 3 - 인터넷 참고
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)