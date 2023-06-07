# [28014] 첨탑 밀어서 부수기
N = int(input())
top_list = list(map(int, input().split()))  # [1 3 2 5 8 1]

count = 1
for i in range(1, N):
    if top_list[i-1] <= top_list[i]:
        count += 1

print(count)
