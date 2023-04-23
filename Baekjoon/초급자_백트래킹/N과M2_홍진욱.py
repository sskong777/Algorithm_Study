n, m = map(int, input().split())
result = []

def backtrack(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            backtrack(i+1)
            result.pop()

backtrack(1)
