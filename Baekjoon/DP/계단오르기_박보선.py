import sys
input = sys.stdin.readline

n = int(input())
    

a = [0]*300
b = [0]*300

b[0] = int(input())

if n == 1:
    print(b[0])
    exit()

a[1] = int(input())
b[1] = a[1] + b[0]

if n == 2:
    print(b[1])
    exit()

for i in range(2, n):
    temp = int(input())
    a[i] = max(a[i-2], b[i-2]) + temp
    b[i] = a[i-1] + temp

print(max(a[n-1], b[n-1]))