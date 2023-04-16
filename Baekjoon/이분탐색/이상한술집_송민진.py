import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
maks = []
for _ in range(n):
    maks.append(int(input()))

if n == k == 1:
    print(maks[0])
else:
    m_sum = sum(maks)
    left, right = 0, max(maks)
    answer = 0
    while left < right:
        mid = (left + right)//2

        cnt = 0
        for i in range(len(maks)):
            if maks[i] > mid:
                cnt += maks[i] // mid

        if cnt >= k:
            answer = mid
            left = mid + 1
        else:
            right = mid

    print(answer)