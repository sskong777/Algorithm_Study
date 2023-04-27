N = int(input())
arr = list(map(int, input().split()))

ans = list()
isUsed = [False for i in range(N)]

max_ = -1

def func(k):
    global max_
    sum = 0
    if k == N:
        for i in range(N - 1):
            sum += abs(ans[i] - ans[i + 1])
        if max_ < sum:
            max_ = sum

    for i in range(N):
        if not isUsed[i]:
            isUsed[i] = True
            ans.append(arr[i])
            func(k + 1)
            isUsed[i] = False
            ans.pop()

func(0)
print(max_)
