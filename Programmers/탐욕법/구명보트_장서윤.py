def solution(people, limit):
    answer = 0

    people.sort()

    l, r = 0, len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        answer += 1

    return answer

'''
people을 정렬한 후, 
투포인터로 가벼운 사람과 무거운 사람의 무게를 계산함
무게합이 limit을 넘지 않는 경우, 다음 사람을 태우기 위해 오른쪽으로 이동해줌
넘는 경우는 자신신보다가벼운 사람의 무게를 비교하기 위해 왼쪽으로 이동해줌
'''
