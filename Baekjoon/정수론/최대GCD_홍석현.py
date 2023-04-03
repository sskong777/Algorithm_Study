import itertools

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

T = int(input())

for tc in range(T):
    arr = list(map(int,input().split()))

    arr_combi = itertools.combinations(arr,2)
    ans = 0
    for i in arr_combi:
        cd = gcd(i[0],i[1])
        ans = max(ans,cd)

    print(ans)
