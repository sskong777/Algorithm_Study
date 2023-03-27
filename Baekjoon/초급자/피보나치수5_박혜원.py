# [10870] 피보나치수5
num = int(input())
num_list = [0, 1]

next_num = 0
for i in range(num-1):
    next_num = num_list[i] + num_list[i+1]
    num_list.append(next_num)

print(num_list[num])
