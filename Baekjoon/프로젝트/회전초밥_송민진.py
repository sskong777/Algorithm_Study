# # 시도 1 - 시간 초과
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().strip().split())
# dict = {}
# for person in range(n):
#     dict[person] = list(map(int, input().strip().split()))[1:]
#
# answer = [0] * n
# for chobab in list(map(int, input().strip().split())):
#     for per in range(n):
#         if chobab in dict[per]:
#             answer[per] += 1
#             dict[per].remove(chobab)
#             break
#
# print(*answer)

# 시도 2
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

c_dict = {}
for person in range(n):
    for chobab in list(map(int, input().strip().split()))[1:]:
        if chobab not in c_dict:
            c_dict[chobab] = [person]
        else:
            c_dict[chobab].append(person)

answer = [0] * n
q = deque(list(map(int, input().strip().split())))
while q:
    now = q.popleft()
    if now in c_dict and len(c_dict[now]) >= 1:
        per = c_dict[now][0]
        answer[per] += 1
        del c_dict[now][0]

print(*answer)