N, M = map(int, input().split())
card = list(map(int, input().split()))

card.sort()

isUsed = [False for _ in range(N + 1)]

ans = list()


def func(k):
    if len(ans) == M:
        print(' '.join(ans))
        return

    for i in range(0, len(card)):
        if not isUsed[i]:
            isUsed[i] = True
            ans.append(str(card[i]))
            func(k + 1)
            isUsed[i] = False
            ans.pop()


func(0)
