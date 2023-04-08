import sys
input = sys.stdin.readline


n, k, b = map(int, input().split())

light = [0 for _ in range(n + 1)]

for _ in range(b):
    i = int(input())
    light[i] = 1


answer = light[1:k+1].count(1)

    
if k == n:
    print(answer)
    exit()

temp = answer
for i in range(2, n - k + 2):
    
    temp -= light[i - 1]
    temp += light[i + k - 1]

    answer = min(answer, temp)

    if answer == -1:
        answer = 0
    
print(answer)