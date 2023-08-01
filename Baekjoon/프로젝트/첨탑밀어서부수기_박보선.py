import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

prev = tower[0]
answer = 0
for i in range(1, n):
    if prev <= tower[i]:
        answer += 1
    prev = tower[i]

print(answer + 1)