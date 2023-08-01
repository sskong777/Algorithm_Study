def solution(nums):
    cnt = len(nums)//2 # 가져 갈 수 있는 포켓몬 수
    poketmon_cnt = len(set(nums)) # 포켓몬 종류
    answer = 0
    if poketmon_cnt > cnt :
        answer = cnt
    else:
        answer = poketmon_cnt
    return answer
