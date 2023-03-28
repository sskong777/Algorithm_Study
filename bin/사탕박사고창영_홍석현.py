
T = int(input())

for tc in range(T):
    space = input()
    r,c = map(int,input().split())
    arr = [list(input()) for _ in range(r)]

    new_arr = list(map(list, zip(*arr)))

    count = 0
    for line in arr:
        for i in range(c):
            if line[i:i+3] ==['>','o','<']:
                count += 1

    for line in new_arr:
        for i in range(r):
            if line[i:i+3] ==['v','o','^']:
                count += 1
    print(count)
