N = int(input())
arr = [int(input()) for _ in range(N)]


def check():
    cnt = 0
    for i in range(1,N):
        if arr[0] > arr[i]:
            cnt += 1
    if cnt == N-1:
        return False
    else:
        return True

ans = 0
while True:
    if check():
        max_index = arr[1:].index(max(arr[1:])) + 1
        arr[max_index] -= 1
        arr[0] += 1
        ans += 1
    else:
        break

print(ans)

