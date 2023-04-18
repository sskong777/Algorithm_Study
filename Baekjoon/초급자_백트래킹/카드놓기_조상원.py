import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

arr = [input().strip() for _ in range(n)]
tot = set()
def backtrack(currlen, toCheck, idxlist):
    if currlen == k:
        if toCheck not in tot:
            tot.add(toCheck)
        return
    
    for i, v in enumerate(arr):
        if i not in idxlist:
            idxlist.append(i)
            newCheck = toCheck + v
            backtrack(currlen+1, newCheck, idxlist)
            idxlist.pop()
        
backtrack(0, "", [])
print(len(tot))