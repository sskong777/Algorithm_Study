import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

for r in arr:
    tmp = [1] * (r+1)
    for i in range(2, r+1):
        for j in range(1, r // i + 1):
            tmp[j*i] = tmp[j*i] ^ 1
    print(sum(tmp[1:]))