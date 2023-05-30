n, k = map(int, input().split())

nums = [i+1 for i in range(n)]
result = []
index = k-1


for i in range(n):
    if len(nums) <= index:
        index %= len(nums)
    result.append(nums.pop(index))
    index += (k-1)

print("<", ', '.join(str(i) for i in result), ">", sep = '')