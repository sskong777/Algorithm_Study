import sys
import math
input = sys.stdin.readline

def isPrime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num %i==0:
            return False
        
    return True

n = int(input())
numbers = list(map(int,input().split()))

count =0
for num in numbers:
    if isPrime(num):
        count +=1
print(count)