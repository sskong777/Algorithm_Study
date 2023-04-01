import math


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def sum_queries(a, d, n):
    return n * (2*a + (n-1)*d) // 2


a, d = map(int, input().split())
q = int(input())
# gcd = gcd(a, d)

for i in range(q):
    x, l, r = map(int, input().split())
    start = a + (l - 1) * d  # 첫째항
    end = a + (r - 1) * d  # 마지막 항

    if x == 1:
        n = r - l + 1
        print(int(sum_queries(a,d,n)))
    elif r == l:
        print(start)
    else:
        print(math.gcd(start,d))


#
# def seq_sum(a, d, n):
#     return n*(2*a + (n-1)*d)//2
#
# a, d = map(int, inp().strip().split())
# N = int(inp())

for _ in range(N):
    # c, l, r = map(int, inp().strip().split())
    a1 = a+d*(l-1)
    if c == 1:
        print(seq_sum(a1, d, r-l+1))
    elif r == l:
        print(a1)
    else:
        print(math.gcd(a1, d))