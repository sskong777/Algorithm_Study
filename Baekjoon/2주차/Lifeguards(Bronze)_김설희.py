n = int(input())
works = []

for _ in range(n):
    works.append(list(map(int, input().split())))

works.sort()

result = 0
for i in range(n):
    total = [0]*1001
    for j in range(n):
        if i == j:
            continue
        for k in range(works[j][0], works[j][1]):
            total[k] = 1
    result = max(result, sum(total))

print(result)
