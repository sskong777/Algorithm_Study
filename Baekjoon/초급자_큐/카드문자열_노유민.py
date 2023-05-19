from collections import deque
import sys

input = sys.stdin.readline
answer = []
t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(ord, input().split()))
    q = deque()
    q.appendleft(l[0])
    for j in range(1, n):
        if l[j] <= q[0]:
            q.appendleft(l[j])
        else:
            q.append(l[j])

    answer.append("".join(list(map(chr, q))))


for i in range(t):
    print(answer[i])
