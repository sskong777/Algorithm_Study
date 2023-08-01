import sys

input = sys.stdin.readline
n = input()
li = list(map(int, input().split()))

u, d = map(int, input().split())

count_1 = li.count(1)
count_2 = li.count(2)

alter_u = u-count_1
alter_d = d-count_2

for i in range(len(li)):
    if li[i] == 1:
        li[i] = 'U'
        u -= 1
    elif li[i] == 2:
        li[i] = 'D'
        d -= 1
    else:
        if alter_u > 0:
            li[i] = 'U'
            u -= 1
            alter_u -= 1
        elif alter_d > 0:
            li[i] = 'D'
            d -= 1
            alter_d -= 1

if u == 0 and d == 0:
    print("YES")
    print(''.join(li))
else:
    print("NO")
