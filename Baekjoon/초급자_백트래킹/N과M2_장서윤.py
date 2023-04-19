N, M = map(int, input().split())

num = list()
isUsed = [False for _ in range(N+1)]

def func(k):
    if len(num) == M:
        print(' '.join(num))
        return

    for i in range(k, N+1):
        if not isUsed[i]:
            num.append(str(i))
            isUsed[i] = True
            func(i+1)
            num.pop()
            isUsed[i] = False


func(1)

