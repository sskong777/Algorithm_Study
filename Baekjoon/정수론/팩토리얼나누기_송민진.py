n, a = map(int, input().strip().split())

cnt = 0
checking = a
while n >= checking:
    cnt += n//checking
    checking *= a

print(cnt)