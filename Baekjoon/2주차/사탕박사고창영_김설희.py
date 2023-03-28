import sys

n = int(input())
for _ in range(n):
    input()
    a, b = map(int, input().split())

    candy = []

    for _ in range(a):
        candy.append(list(sys.stdin.readline().rstrip()))

    cnt = 0
    for i in range(a):
        for j in range(1, b-1):
            if candy[i][j] == 'o' and candy[i][j-1] == '>' and candy[i][j+1] == '<':
                cnt += 1

    for i in range(1, a-1):
        for j in range(b):
            if candy[i][j] == 'o' and candy[i-1][j] == 'v' and candy[i+1][j] == '^':
                cnt += 1

    print(cnt)