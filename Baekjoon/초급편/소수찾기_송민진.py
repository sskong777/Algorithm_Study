import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
answer = 0

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for num in arr:
    if is_prime(num):
        answer += 1

print(answer)