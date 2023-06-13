import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())

mission = list(map(int, input().split())) + list(map(int, input().split()))

order = [0, 1, 2, 3, 4, 5]

missionList = list(product(order, repeat=n))

answer = 0

for missionOrder in missionList:
    total = 0
    prev = -1
    
    for i in missionOrder:
        
        if prev == i or prev == (i + 3) % 6:
            total = total + (mission[i] // 2)
        else:
            total = total + mission[i]
            prev = i

    if total >= m:
        answer += 1

print(answer)

    
    