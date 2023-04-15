num = list(map(int,input().split()))

min_ = min(num)

while True:
    cnt = 0
    for i in range(5):
        if min_ % num[i] == 0:
            cnt +=1

    if cnt >= 3:
        print(min_)
        break

    min_+=1

