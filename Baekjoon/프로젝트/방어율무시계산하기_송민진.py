import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
score = 0.0

for i in range(n):
    score = 100 - ((100 - score) * (100 - arr[i]) / 100)
    print(score)