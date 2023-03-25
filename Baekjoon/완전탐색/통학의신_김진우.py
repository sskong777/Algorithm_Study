a, b = map(int, input().split())
li = []
for x in range(-1000,1001):
    if x*x + 2*a*x + b == 0:
        li.append(x)

print(*sorted(li))