import sys
input = sys.stdin.readline

mushroom = []

for i in range(10):
    t = int(input())
    if i == 0:
        mushroom.append(t)
    else:
        mushroom.append(mushroom[i-1] + t)

answer = 0
flag = True
for i in range(10):
    if mushroom[i] >= 100:
        a = abs(100 - mushroom[i])
        b = abs(100 - mushroom[i - 1])
        
        if a == b:
            answer = max(mushroom[i], mushroom[i-1])
        else:
            if a < b:
                answer = mushroom[i]
            elif a > b:
                answer = mushroom[i-1]
        flag = False
        break

if flag:
    print(max(mushroom))
else:
    print(answer)