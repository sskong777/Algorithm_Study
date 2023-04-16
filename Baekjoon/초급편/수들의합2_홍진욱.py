n = list(map(int, input().split()))
n_list = list(map(int, input().split()))

left = 0
right = 0
sum_value = 0
result = 0

while left < n[0]:
    if sum_value < n[1]:
        if right < n[0]:
            sum_value += n_list[right]
            right += 1
        else:
            break
    elif sum_value == n[1]:
        result += 1
        sum_value -= n_list[left]
        left += 1
    else:
        sum_value -= n_list[left]
        left += 1

print(result)
