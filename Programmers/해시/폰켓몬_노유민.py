def solution(nums):
    answer = 0
    want = len(nums)/2
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    can = len(dic)
    if want <= can:
        answer = want
    else:
        answer = can
    return answer
