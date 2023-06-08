import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

if a + (b*7) > 30:
    print(0)
else:
    print(1)