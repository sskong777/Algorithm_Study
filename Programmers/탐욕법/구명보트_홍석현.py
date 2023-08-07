# 몸무게순으로 정렬하여
# 몸무게 가장 작은 사람과 가장 큰 사람을 더해 둘 다 탈 수 있으면 둘 다 태우고,
# limit을 초과하면 몸무게 큰 사람만 태운다.

def solution(people, limit):
    answer = 0

    people.sort()

    start, end = 0, len(people) - 1

    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return answer

# def solution(people, limit):
#     answer = 0

#     people.sort()


#     while len(people) > 2:
#         answer += 1
#         if people[0] + people[-1] <= limit:
#             people.pop(0)
#         people.pop()

#     return answer
