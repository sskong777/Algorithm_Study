from itertools import product

n, m = map(int, input().split())

works =[]

for _ in range(2):
    works+=list(map(int, input().split()))

products = list(product([0,1,2,3,4,5], repeat=n))

count = 0
for p in products:
    total = 0
    prev = -1
    for i in p:
        if prev == i or prev == (i + 3) % 6:
            total += (works[i]//2)
        else:
            total += works[i]
        prev = i
    if total >=m :
        count+=1
print(count)