import sys
input = sys.stdin.readline

n, x = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

w = 0

for a, b in zip(A, B):
    w += b
    
    if w < a:
        print(-1)
        exit()
    
print((w - A[-1]) // x)