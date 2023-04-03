# [10162] 전자레인지

time = int(input())
operate_time = [300, 60, 10]

answer = []
count = 0

if time % 10 != 0:
    print(-1)
else:
    for i in operate_time:
        count = time // i
        answer.append(count)
        time %= i
    print(answer[0], answer[1], answer[2], sep=" ")
