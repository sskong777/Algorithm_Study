import sys

n, m = map(int, sys.stdin.readline().split())

arr =list(map(int,sys.stdin.readline().split()))

arr.sort()
combi = []
def backtrack(currlen):
    if currlen == m:
        print(' '.join(map(str, combi)))
        return
    
    for num in arr:
        if num not in combi:
            combi.append(num)
            backtrack(currlen+1)
            combi.pop()
            
backtrack(0)