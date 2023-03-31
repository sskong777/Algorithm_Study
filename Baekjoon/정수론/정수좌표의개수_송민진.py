# 시도 2 - x사이 거리, y 사이의 거리의 GCD+1 = 개수
n, m, k = map(int, input().strip().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

answer = 0
for x1 in range(n+1):
    for y1 in range(m+1):
        for x2 in range(n+1):
            for y2 in range(m+1):
                if gcd(abs(x1-x2), abs(y1-y2)) + 1 == k:
                    answer += 1

print(answer // 2)