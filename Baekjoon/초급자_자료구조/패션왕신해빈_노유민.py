import sys

input = sys.stdin.readline

t = int(input())
result = []
for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        value = input().rstrip()
        wear = list(value.split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    count = 1

    for k in weardict:
        count *= (len(weardict[k])+1)
    result.append(count-1)

for i in result:
    print(i)
