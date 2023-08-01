import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

m = -1
ret = int(1e9)

for i in range(len(arr)-1):
    l, h = arr[i], arr[i+1]
    # print('-------------')
    # print(l, h)
    tmp = l+1
    while tmp < h:
        # print(tmp)
        c = min(abs(tmp-l), abs(h-tmp))
        # print('c', c)
        if c > m:
            m = c
            ret = tmp
        elif c == m:
            if tmp < ret:
                ret = tmp
        # print('ret', ret)
        tmp+=1

# print('ret', ret)
if ret == int(1e9):
    print(-1)
else:
    print(ret)