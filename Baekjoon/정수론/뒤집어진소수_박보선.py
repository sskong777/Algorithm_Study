import sys
import math
input = sys.stdin.readline

def rotate(n_list):
    n = len(n_list)
    prev = [0 for _ in range(n)]
    
    for i in range(n):
        prev[n - 1 - i] = n_dict[n_list[i]]
    
    prevNum = int(''.join(prev))
    
    return isPrime(prevNum)
    
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

before = False
after = False

n_dict = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}

n = int(input())
n_list = list(str(n))

if n == 2 or n == 5:
    print('yes')
    exit()

if '3' in n_list or '4' in n_list or '7' in n_list or n_list[0] in ['5', '9', '8']:
    print('no')
    exit()

before = isPrime(n)
after = rotate(n_list)

if before and  after:
    print('yes')
else:
    print('no')

