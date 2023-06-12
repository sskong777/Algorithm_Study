import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

person = [0 for _ in range(n)]
temp = [0 for _ in range(n)]
for i in range(m):
    p = int(input())
    person[p] = 1

for i in range(k):
    
    for j in range(n):
        if person[j] == 1:
            temp[(j - 1) % n] = (temp[(j - 1) % n] + 1) % 2
            temp[(j + 1) % n] = (temp[(j + 1) % n] + 1) % 2

    person = temp[:]
    temp = [0 for _ in range(n)]
    
print(person.count(1))