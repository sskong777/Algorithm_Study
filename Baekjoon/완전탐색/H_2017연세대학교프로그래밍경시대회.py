# # 시도 1
# import itertools
# n = int(input()) - 3    # 최소 1개씩은 가져야 하기 때문
#
# pers = list(map(list, itertools.permutations([i for i in range(n)], 3)))
# answers = []
#
# for per in pers:
#     if sum(per) == n:
#         if per[2] % 2 == 1:
#             if per[0] >= per[1]+2:
#                 answers.append(per)
#
# print(len(answers))

# 시도 2
n = int(input())
cnt = 0

for a in range(n):
    for b in range(n):
        for c in range(n):
            if a + b + c == n:
                if a >= b+2 and b >= 1 and c >= 1:
                    if c % 2 == 0:
                        cnt += 1

print(cnt)