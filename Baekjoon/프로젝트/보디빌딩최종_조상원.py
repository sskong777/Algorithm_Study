import sys

input = sys.stdin.readline

t, x = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


n = 0
w = 0

for i in range(t):
    w += b[i]
    if a[i] > b[i]:
        if a[i] > w:
            n=-1
            break

if n != -1:
    n += (w - a[-1]) // x            

print(n)