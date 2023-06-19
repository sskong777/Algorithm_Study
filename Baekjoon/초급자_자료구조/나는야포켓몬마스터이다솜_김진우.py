'''import sys
input = sys.stdin.readline
n, m = map(int, input().split())
poketmon = [input().rstrip() for _ in range(n)]
arr = [input().rstrip() for _ in range(m)]

for i in arr:
    if i.isdigit():
        print(poketmon[int(i)])
    else:
        print(poketmon.index(i) + 1)'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())


poketmon_dict = {}
poketmon_list = []
for i in range(1, n+1):
    name = input().rstrip()
    poketmon_dict[name] = i
    poketmon_list.append(name)


output = []
for _ in range(m):
    query = input().rstrip()
    if query.isdigit():
        output.append(poketmon_list[int(query) - 1])
    else:
        output.append(str(poketmon_dict[query]))


sys.stdout.write('\n'.join(output))
