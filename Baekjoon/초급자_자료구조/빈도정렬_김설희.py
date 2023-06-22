n, c = map(int, input().split())
nums = list(map(int, input().split()))

dic = {}

for i in nums:
    if i not in dic:
        dic[i] = nums.count(i)

sorted_dic = sorted(dic.items(), key = lambda x : (-x[1], list(dic.keys()).index(x[0])))

result = []
for i in sorted_dic:
    for _ in range(i[1]):
        result.append(i[0])

print(*result)

