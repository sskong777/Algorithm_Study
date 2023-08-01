import sys
sys.stdin = open('input.txt')
N, M, K = map(int, input().split())
P = [0] * N
for p in sys.stdin.readlines():
    P[int(p)] = 1

def eungae():
    global P
    tmp = [0] * N
    for i in range(N):
        if not P[i]: continue
        tmp[(i - 1) % N] = (tmp[(i - 1) % N] + 1) % 2
        tmp[(i + 1) % N] = (tmp[(i + 1) % N] + 1) % 2
    P = tmp
    return sum(tmp)

pattern = [M]
for _ in range(K):
    pattern.append(eungae())
print(" ".join(map(str, pattern)))
# print(pattern[K], pattern[K%N], pattern[K%N] == pattern[K])