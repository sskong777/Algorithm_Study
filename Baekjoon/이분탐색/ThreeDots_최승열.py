# [13423] Three Dots
# https://www.acmicpc.net/problem/13423

for _ in range(int(input())):
    N = int(input())
    P = sorted(map(int, input().split()))
    pset = set(P)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if 2*P[j]-P[i] in pset: ans += 1
    print(ans)
