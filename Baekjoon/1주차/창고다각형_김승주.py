import sys
input = sys.stdin.readline

def calculate_left():
    cur_max = storages[0][1]
    sum = 0
    for i in range(storages[0][0], max_l):
        for storage in storages:
            if storage[0] == i:
                cur_max = max(storage[1], cur_max)
        sum += cur_max
    return sum


def calculate_right():
    cur_max = storages[-1][1]
    sum = 0
    for i in range(storages[-1][0], max_l, -1):
        for storage in storages:
            if storage[0] ==i:
                cur_max = max(storage[1], cur_max)
        sum+= cur_max
    return sum

n = int(input())
storages = []
for _ in range(n):
    l,h = map(int,input().split())
    storages.append((l,h))

storages.sort(key = lambda x : x[0])
max_l, max_h = max(storages, key = lambda x :x[1])

ans = calculate_left() + calculate_right() + max_h
print(ans)


