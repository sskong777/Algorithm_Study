# [28075]스파이

"""
 민겸이가 전날에 임무를 수행한 곳과 같은 장소를 선택하면 그 날은 원래의 절반에 해당하는 진척도만 얻을 수 있다
 이때, 장소가 같다면 임무가 달라도 얻는 진척도는 원래의 절반이 됨

 기여도(M) = 진척도의 합

 M 이상의 기여도를 얻을 수 있는 임무 수행 방법이 몇 가지인지?

임무를 수행하는 총 일수 N
민겸이가 얻고 싶은 최소 기여도 M
info = 수족관, 시청, 학교
watch = 수족관, 시청, 학교
"""
from itertools import product

N, M = map(int, input().split())
info = list(map(int, input().split()))
observe = list(map(int, input().split()))

#  6가지 임무를, repeat=N은 N일 동안
tasks = info + observe

schedules = list(product(range(6), repeat=N))

count = 0
for schedule_idx, schedule in enumerate(schedules):
    print(f"\nProcessing schedule {schedule_idx+1}: {schedule}")
    last_day_place = [-1]*6
    total_score = 0
    for i, task in enumerate(schedule):
        place = task % 3
        print(f"\tDay {i+1}, Task {task}, Place {place}")
        if last_day_place[place] == task:  # 전날에 같은 장소에서 작업했다면
            total_score += tasks[task]//2
            print(f"\t\tSame place as yesterday. Half score: {tasks[task]//2}")
        else:  # 전날에 다른 장소에서 작업했다면
            total_score += tasks[task]
            print(
                f"\t\tDifferent place than yesterday. Full score: {tasks[task]}")
        last_day_place[place] = task
    if total_score >= M:  # 기여도가 M 이상이면
        count += 1
        print(
            f"\tTotal score: {total_score}. Achieved target! Current count: {count}")
    else:
        print(f"\tTotal score: {total_score}. Did not achieve target.")
print(f"\nFinal count: {count}")
