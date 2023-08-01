N, X = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
def run():
    W = 0
    for i in range(N):
        W += B[i]
        if (A[i] > W): return -1
    return (W-A[-1]) // X
print(run())