# [1806] 부분합
n, s = map(int, input().split())
num_list = list(map(int, input().split()))

start, end = 0, 1
check = True
answer = []
while start < end:
    interval_sum = sum(num_list[start:end])
    if interval_sum < s:
        end += 1
    elif interval_sum > s:
        start += 1
    else:
        answer.append(len(num_list[start:end]))
        check = False
        print(answer)
        break

if check == True:
    print(-1)
# print(sum(num_list[start:end]))
