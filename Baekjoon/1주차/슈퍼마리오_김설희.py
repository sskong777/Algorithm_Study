import sys

score = []
ans = []

for _ in range(10):
    s = int(sys.stdin.readline())
    score.append(s)

for i in range(len(score)):
    sum = 0
    for j in range(0, i + 1):
        sum += score[j]
    ans.append(sum)

diff = [abs(i-100) for i in ans]
m = diff.index(min(diff))

print(ans[m+1]) if diff.count(min(diff)) > 1 else print(ans[m])
