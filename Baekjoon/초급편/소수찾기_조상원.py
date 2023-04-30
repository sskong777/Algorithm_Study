import sys
num = int(input())
arr = list(map(int, sys.stdin.readline().split()))


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


c = 0
for n in arr:
    if is_prime(n):
        c += 1

print(c)
