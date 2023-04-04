import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

tmp = arr[0]
left = 0
right = 1
cnt = 0

while True:
    if tmp < m:
        if right < n:
            tmp += arr[right]
            right += 1
        else:
            break
    elif tmp == m:
        cnt += 1
        tmp -= arr[left]
        left += 1
    else:
        tmp -= arr[left]
        left += 1

print(cnt)