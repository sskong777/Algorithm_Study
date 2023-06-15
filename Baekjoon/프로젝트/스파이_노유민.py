from itertools import product

n, m = map(int, input().split())

li = []
for _ in range(2):
    values = list(map(int, input().split()))
    li+=values
cases = list(product([0,1,2,3,4,5], repeat=n))

count = 0
for i in cases:
    totalCount = 0
    past = -1
    for j in i:
        if past == j or past == (j + 3) % 6:
            totalCount += (li[j]//2)
        else:
            totalCount += li[j]
        past = j
    if totalCount >=m :
        count+=1
print(count)