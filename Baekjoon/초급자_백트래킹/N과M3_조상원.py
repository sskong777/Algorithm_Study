import sys

n, m = map(int, sys.stdin.readline().split())

combi = []
def backtrack(currlen):
    if currlen == m:
        print(' '.join(map(str, combi)))
        return
    for i in range(1, n+1):
        combi.append(i)
        backtrack(currlen+1)
        combi.pop()

backtrack(0)