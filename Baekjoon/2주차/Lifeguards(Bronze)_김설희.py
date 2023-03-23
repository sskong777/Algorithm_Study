n = int(input())
works = []

for _ in range(n):
    x, y = map(int, input().split())
    works.append([i for i in range(x, y)])


count = [0]*1001
for work in range(n):
    for i in work:
        count[i] = 1

print(sum(count))



print(works)