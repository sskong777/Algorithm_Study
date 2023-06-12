N = int(input())

level = list(map(int, input().split()))
level.sort()

ok = False
ans = 0
max_ = -1

for i in range(1, N):
    start = level[i-1]
    end = level[i]
    for j in range(start+1, end):
        if j - start > max_ and  end - j > max_:
            max_ = j - start
            ans = j
            ok = True
    else:
        continue

if ok:
    print(ans)
else:
    print(-1)
