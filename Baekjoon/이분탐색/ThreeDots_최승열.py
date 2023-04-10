# [13423] Three Dots
# https://www.acmicpc.net/problem/13423

T = int(input())
for _ in range(T):
    N = int(input())
    P = set(map(int, input().split()))
    ans = 0
    for p in P:
        for c in P:
            if p >= c: continue
            if 2*c-p in P: ans += 1
    print(ans)
