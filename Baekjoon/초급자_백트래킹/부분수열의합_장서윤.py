N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0


def func(k, idx, sum):
    global cnt

    if sum == S and idx > 0:  # 탈출
        cnt += 1

    for i in range(k, len(arr)):
        sum += arr[i]
        func(i + 1, idx + 1, sum)
        sum -= arr[i]


func(0, 0, 0)
print(cnt)
