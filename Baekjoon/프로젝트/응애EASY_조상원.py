import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] * n
tmp = []

for _ in range(m):
    c = int(input())
    arr[c] = 1
for _ in range(k):
    for i in range(len(arr)):
        if i == len(arr)-1:
            a, b = arr[i-1], arr[0]
        else:
            a, b = arr[i-1], arr[i+1]

        if (a == 1 and b == 0) or (a == 0 and b == 1):
            tmp.append(1)
        elif (a == 1 and b == 1) or (a == 0 and b == 0):
            tmp.append(0)
    arr.clear()
    arr = tmp[:]
    tmp.clear()

print(sum(arr))
