import  math

n, m = map(int,input().split())
# n : 아이들수 , m : 보석수
jew = [int(input()) for _ in range(m)]

low = 1
high = max(jew)
dab = 999999999
while low <= high:
    tmp = 0
    mid = (low + high) // 2
    for i in jew:
        tmp += math.ceil(i / mid)

    if tmp > n:
        low = mid + 1
    else:
        high = mid - 1
        dab = min(dab, mid)

print(dab)