import sys
N, M, K = map(int, sys.stdin.readline().split())
_max = 0
for i in range(K+1):
    _max = max(min((N-i)//2, M-K+i), _max)
print(_max)