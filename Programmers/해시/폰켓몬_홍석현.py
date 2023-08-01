def solution(nums):
    len_nums = len(nums) / 2  # 고를 폰켓몬의 수
    set_nums = set(nums)
    len_set_nums = len(set_nums)  # 중복제거한 폰켓몬 수

    # 고를 포켓몬 수가 더 적으면
    if len_nums <= len_set_nums:
        answer = len_nums
    # 중복 제거한 폰켓몬 수가 더 적으면
    else:
        answer = len_set_nums
    return answer