n, m = map(int, input().split())
result = []

def backtrack(start, cnt):
    if cnt == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
            result.append(i)
            backtrack(i, cnt+1)
            result.pop()

backtrack(1, 0)
