n, m, k = map(int, input().split())
people = [0] * n
result = [0] * n

for _ in range(m):
    people[int(input())] = 1

for _ in range(k):
    result = [0] * n

    for i in range(n):
        if people[i] == 1:
            result[i-1] = (result[i-1] + 1) % 2
            result[(i+1) % n] = (result[(i+1) % n] + 1) % 2

    people = result

print(sum(people))





