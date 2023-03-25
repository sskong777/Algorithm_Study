# # 시도 1 - 92%에서 틀렸습니다 뜸
# from itertools import combinations
#
# n = int(input())
# sams = []
# answer_pools = []
#
# i = 0
# while (3**i) <= 2147483647:
#     sams.append(3**i)
#     i += 1
#
# for k in range(1, len(sams)):
#     samsams = list(map(list, combinations(sams, k)))
#     for ss in samsams:
#         answer_pools.append(sum(ss))
#
# if n in answer_pools:
#     print("YES")
# else:
#     print("NO")

# 시도 2
n = int(input())
samsam = True

if n == 0:
    samsam = False

while n > 0:
    if n % 3 == 2:
        samsam = False
    n //= 3

print("YES" if samsam else "NO")