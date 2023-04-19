import sys

n, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n+1)]
combi = []
def backtrack(currlen, start):
    if currlen == m:
        print(' '.join(map(str, combi)))
        return
    
    for i in range(start, n+1):
        if i not in combi:
            combi.append(i)
            backtrack(currlen+1, i+1)
            combi.pop()

backtrack(0, 1)