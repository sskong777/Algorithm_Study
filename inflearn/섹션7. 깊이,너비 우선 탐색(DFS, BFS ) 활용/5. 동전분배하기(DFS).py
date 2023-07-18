'''
input
7
8
9
11
12
23
15
17

output
5
'''
import sys

def dfs():
    return

input = sys.stdin.readline
n = int(input())
coins = []
for _ in range(n):
    coins.append(int(input()))
result = [0] * n

print(coins)