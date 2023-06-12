import sys
input = sys.stdin.readline

n = int(input())
locs = list(map(int, input().strip().split()))
lengths = list(map(int, input().strip().split()))
colors = list(input().strip().split(' '))

answers = []
for i in range(n):
    for j in range(i+1, n):
        if abs(locs[j] - locs[i]) <= lengths[j] + lengths[i]:
            if colors[i] != colors[j]:
                answers = [i+1, j+1]
                break
    if answers:
        break

if not answers:
    print("NO")
else:
    print("YES")
    print(*answers)