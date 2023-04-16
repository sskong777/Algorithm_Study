N, M = map(int, input().split())
A = list(map(int, input().split()))


start, end = 0, 1
cnt = 0

while start <= end:

    if end > N:
        break

    s = sum(A[start:end])

    if s == M:
        start += 1
        end = start + 1
        cnt += 1
    elif s > M:
        start += 1
    else:
        end += 1

print(cnt)