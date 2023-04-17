N = int(input())


def num():
    s, e = 0, 1
    cnt = 0
    sum = 1

    while s <= e:
        if sum == N:
            cnt += 1
            e += 1
            sum += e

        elif sum < N:
            e += 1
            sum += e

        elif sum > N:
            sum -= s
            s += 1
    return cnt

print(num())