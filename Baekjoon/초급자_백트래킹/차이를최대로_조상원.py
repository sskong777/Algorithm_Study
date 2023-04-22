import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

total = 0


def backtrack(currlst):
    global total
    if len(currlst) == n:
        currsum = 0
        for i in range(n-1):
            currsum += abs(arr[currlst[i]] - arr[currlst[i+1]])
        total = max(currsum, total)
        return

    for i in range(n):
        if i not in currlst:
            currlst.append(i)
            backtrack(currlst)
            currlst.pop()


backtrack([])
print(total)
