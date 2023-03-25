a, b, n, w = map(int, input().split())
answer = []
for x in range(1, n):
    if (a * x) + (b * (n-x)) == w:
        answer.append((x, n-x))

if len(answer) == 0 or len(answer) >= 2:
    print(-1)
else:
    a, b = answer[0]
    print(a, b)
