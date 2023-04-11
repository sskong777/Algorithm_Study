import sys
input = sys.stdin.readline

X = list()

def binary_search(a, b, c):
    cnt = 0
    while a != c:
        m = a + (c - a) // 2
        if X[m] == b:
            c = m
            cnt +=1
        else:
            a = m + 1
    return cnt


T = int(input())

for i in range(T):
    N = int(input().rstrip())
    X = list(map(int, input().rstrip().split()))
    X.sort()

    cnt = 0

    for l in range(N):
        for r in range(l + 1, N):
            cnt += binary_search(l, X[l] + X[r] // 2, r)

    print(cnt)
