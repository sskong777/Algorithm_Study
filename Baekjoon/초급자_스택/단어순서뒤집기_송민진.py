import sys
input = sys.stdin.readline

n = int(input())
for tc in range(n):
    arr = list(input().strip().split())
    arr.reverse()
    print("Case #" + str(tc+1) + ":", end=" ")
    print(*arr)
