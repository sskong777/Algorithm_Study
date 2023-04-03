
import sys
from itertools import combinations
input = sys.stdin.readline

def find_gcd(i,j):
    x,y = min(i,j), max(i,j)
    ans = 0
    for i in range(1,x+1):
        if x%i ==0 and y%i==0:
            ans = max(ans,i)
    return ans

n = int(input())

for t in range(n):
    numbers = list(map(int,input().split()))

    num_combi = list(combinations(numbers,2))

    ans = 0
    for i,j in num_combi :
        ans = max(ans,find_gcd(i,j))
    print(ans)