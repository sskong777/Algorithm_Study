# [6219] 소수의 자격 (실버 3)
## pypy3만 가능 (python3 시간초과)
import math
A, B, D = map(int, input().split())

def isPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True

cnt = 0
for num in range(A, B+1):
    if isPrime(num):
        if str(D) in str(num):
            cnt += 1

print(cnt)