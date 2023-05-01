start, end = map(int, input().split())

num_list =[]

for i in range(1, end+1):
    for j in range(i):
        num_list.append(i)
print(sum(num_list[start-1:end]))

