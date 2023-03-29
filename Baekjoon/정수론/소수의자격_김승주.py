'''
문제 : 소수의 자격
'''
import math
import sys
input = sys.stdin.readline

def check_prime(num):
    if num <=1:
        return False
    if num ==2:
        return True
    if num %2==0:
        return False
    
    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i ==0:
            return False
    return True

a,b,d = map(int,input().split())

count = 0
for i in range(a, b+1):
    if str(d) in str(i):
        if check_prime(i):
            count+=1
print(count)