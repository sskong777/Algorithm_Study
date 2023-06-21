import sys
from collections import Counter

input = sys.stdin.readline


n, c = map(int, input().split())

arr = list(map(int, input().split()))

l = Counter(arr)

ret = []

for a, b in l.most_common():
    for _ in range(b):
        ret.append(str(a))
print(' '.join(ret))
