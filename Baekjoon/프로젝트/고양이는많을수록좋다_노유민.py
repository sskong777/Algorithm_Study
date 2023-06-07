import sys

input = sys.stdin.readline
n = int(input())

count = 0

while(n > 3):
    count += 1
    n = n//2 + (1 if n % 2 == 1 else 0)

print(count+n)
