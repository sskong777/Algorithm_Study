import sys

n = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))
test.sort()

check = False
ans = 0
diff = -1

for i in range(1, n):
    start = test[i-1]
    end = test[i]
    for j in range(start + 1, end):
        if j - start > diff and end - j > diff:
            diff = j - start
            ans = j
            check = True


if check:
    print(ans)
else:
    print(-1)