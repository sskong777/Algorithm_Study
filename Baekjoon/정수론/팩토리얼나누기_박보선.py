import sys
input = sys.stdin.readline

n, a = map(int, input().split())

cnt = 0
t = a

while t <= n:
    cnt += n // t
    t *= a

print(cnt)