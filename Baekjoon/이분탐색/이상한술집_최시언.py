num_kettles, num_people = map(int, input().split())
kettle_capacities = [int(input()) for _ in range(num_kettles)]

start_cap = 1
end_cap = max(kettle_capacities)
max_distributed_cap = 0

while start_cap <= end_cap:
    mid_cap = (start_cap + end_cap) // 2
    total_distributed_cap = sum(n // mid_cap for n in kettle_capacities)
    
    if total_distributed_cap >= num_people:
        max_distributed_cap = mid_cap
        start_cap = mid_cap + 1
    else:
        end_cap = mid_cap - 1

print(max_distributed_cap)
