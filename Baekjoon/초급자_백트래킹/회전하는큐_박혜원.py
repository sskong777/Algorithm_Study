# [1021] 회전하는큐
"""
q가 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 라면,
뽑아내려고 하는 수 첫번째 수가 앞쪽에 더 가까우면 -> 왼쪽으로 한칸 이동시키는 연산을 수행
두번쨰로 뽑아내려는 수가 뒤쪾에 더 가깝다면 오른쪽으로 한칸 이동시키는 연산을 수행해준다.
큐의 크기 N과 뽑아내려고 하는 수의 개수 M
"""
from collections import deque


n, m = map(int, input().split())  # 10, 3
location = list(map(int, input().split()))  # [2, 9, 5]
nums = [i for i in range(1, n + 1)]  # [1,2,3,4,5,6,7,8,9,10]
q = deque(nums)

count = 0

for i in location:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            # 오른쪽으로 보내기
            if q.index(i) > len(q)//2:
                q.rotate(1)
                count += 1
            else:
                # 왼쪽으로보내기
                q.rotate(-1)
                count += 1

print(count)
