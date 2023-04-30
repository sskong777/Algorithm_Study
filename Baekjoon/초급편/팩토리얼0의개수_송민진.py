n = int(input())

tmp = 1
for i in range(2, n+1):
    tmp *= i

cnt = 0
for idx in range(len(str(tmp))-1, -1, -1):
    if str(tmp)[idx] == "0":
        cnt += 1
    else:
        print(cnt)
        break