N, M = map(int, input().rstrip().split())
X = list(map(int, input().rstrip().split()))
X.sort()


def cutting(h):
    s = 0
    for i in range(N):
        if X[i] > h:
            s += X[i] - h
    return s


def binary(l, r):

    if N==1:
        return X[0]- M

    while l != r:
        m = r - (r - l) // 2

        if M <= cutting(m):
            l = m
        else:
            r = m - 1
    return l


print(binary(X[0]-1, X[N - 1]))

'''
3 1
10 10 10
9

4 10
4 5 6 7
3

5 23
50 32 48 28 10

2 10000
10001 20000
10000

1 11
106
95
'''