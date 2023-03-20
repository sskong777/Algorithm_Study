n, k = map(int, input().split())
temp = list(map(int, input().split()))

const = []

for i in range(n - (k-1)):
    sum = 0
    for j in range(i, i + k):
        sum += temp[j]
    const.append(sum)

print(max(const))
