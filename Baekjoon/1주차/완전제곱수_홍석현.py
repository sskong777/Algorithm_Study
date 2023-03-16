N = int(input())

count = 0
for a in range(500,1,-1):
    for b in range(1,a):
        if b >= a:
            break
        if a == ((b**2 + N))**0.5:
            count += 1
print(count)