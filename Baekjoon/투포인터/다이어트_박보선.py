import sys
input = sys.stdin.readline

g = int(input())

kg = []

def solution():
    for i in range(1, g):
        prev = i ** 2
        for j in range(i + 1, g + 1):
            temp = (j ** 2) - prev

            if j == i + 1:
                if temp > g:
                    return
            if temp == g:
                kg.append(j)
                break
            elif temp > g:
                break
            
solution()

if len(kg) == 0:
    print(-1)
else:
    kg.sort()
    print(*kg)