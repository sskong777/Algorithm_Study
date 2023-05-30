import sys

N=int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

result = 0.0

for i in range(N):
    result = 1 - (1 - result) * (1 - num[i] / 100)
    print(round(result * 100,6))


