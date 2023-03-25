# [2563] 색종이 (실버 5)
import sys
input = sys.stdin.readline

paper = [[0]*101 for _ in range(101)]
N = int(input())

for n in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] > 0:
            cnt+=1

print(cnt)