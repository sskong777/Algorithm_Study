import sys
import math
input = sys.stdin.readline

a, b, d = map(int, input().split())
d = str(d)
answer = 0
def isPrime(n):
    if n <= 1: 
        return False
 
    if n % 2 == 0: 
        if n == 2:
            return True
        else:
            return False
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    
    return True

for i in range(a, b + 1):
    if d in str(i):
        if isPrime(i):
            answer += 1
            
print(answer)