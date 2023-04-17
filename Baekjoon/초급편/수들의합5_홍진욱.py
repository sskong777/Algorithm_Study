n = int(input())

start = 1
end = 1
sum_value = 1
count = 0

while start <= n:
    if sum_value == n:
        count += 1
        sum_value -= start
        start += 1
    elif sum_value < n:
        end += 1
        if end > n:
            break
        sum_value += end
    else:
        sum_value -= start
        start += 1

print(count)
