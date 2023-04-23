import sys

n, m = map(int, sys.stdin.readline().split())

combi = []
def backtrack(currlen, start):
    if currlen == m:
        print(' '.join(map(str, combi)))
        return
    
    for i in range(start, n+1):
        combi.append(i)
        backtrack(currlen+1, i)
        combi.pop()
        
backtrack(0, 1)