num_list = list(map(int, input().split()))
checking = 1

while True:
    cnt = 0
    for num in num_list:
        if checking % num == 0:
            cnt += 1
    if cnt >= 3:
        print(checking)
        break
    checking += 1