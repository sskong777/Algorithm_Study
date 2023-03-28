li = [int(input()) for _ in range(10)]


cnt = 0
for i in li:
    cnt += i
    print(cnt)
    if cnt >= 100:
        if cnt - 100 > 100 - (cnt - i):
            cnt -= i
        break


print(cnt)
