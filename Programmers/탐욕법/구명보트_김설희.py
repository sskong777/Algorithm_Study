# 효율성 테스트 시간 초과
'''
def solution(people, limit):

    people.sort()
    cnt = 0

    # 어차피 최대 2명임
    while people:
        if people[0] + people[-1] <= limit and len(people) > 1: # 테케2 때문에 추가 조건 달았음
            people = people[1:] # people.pop(0)랑 똑같은데 효율 더 낫대서
        people.pop() # 원래 if else 문으로 했는데 얘네가 중복되는 코드
        cnt += 1

    return cnt
'''

# 이진 탐색으로~
def solution(people, limit):

    people.sort()
    cnt = 0

    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1

    return cnt

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))