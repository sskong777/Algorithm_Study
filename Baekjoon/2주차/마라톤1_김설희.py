n = int(input())
point = []

def checkDiff(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

for i in range(n):
    point.append(list(map(int, input().split())))

total = 0
for i in range(1, n):
    total += checkDiff(point[i], point[i-1])

ans = []
for i in range(1, n-1):
    check = total - (checkDiff(point[i], point[i-1]) + checkDiff(point[i], point[i+1]) - checkDiff(point[i+1], point[i-1]))
    ans.append(check)

print(min(ans))